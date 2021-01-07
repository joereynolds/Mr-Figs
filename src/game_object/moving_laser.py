"""
An enemy that follows a pre-determined path
"""

import pygame
from pygame.math import Vector2
import src.interpolate as interpolate
from src.game_object.path import Path
from src.game_object.solid_tile import SolidTile
from src.entity import Entity
import src.colours as colours
import src.graphics as graphics
import time
import random

class MovingLaser(Entity):
    """An almost exact copy of enemy pathable. If we can do it in a clean way,
    consider extending it instead and writing the laser logic separately."""

    def __init__(
            self, 
            x: int, 
            y: int, 
            width: int, 
            height: int, 
            path: Path, 
            level, #: TiledMap,
            speed: int = 2,
            image=None,
        ):
        Entity.__init__(self, x, y, width, height, image)
        self.minimap_colour = colours.RED_HIGHLIGHT
        self.path = path
        self.destination = path.points[-1]
        self.processed_points = []
        self.position = Vector2(x, y)
        self.vel = Vector2(0, 0)
        self.target = self.path.points[1]
        self.target_radius = 25
        self.speed = speed
        self.waypoint_index = 0
        self.level = level
        self.lasers = pygame.sprite.LayeredUpdates()
        self.range = 25
        self.speed = 0.5


    def round_to_nearest_tile(self, x, base = graphics.tile_width):
        return base * round(x/base)

    def update(self, delta_time):

        for i in range(self.range):
            laser = Line(
                self.rect.x, 
                self.rect.y - (i * graphics.tile_height),
                2, 
                graphics.tile_height
            )

            nearest_x = self.round_to_nearest_tile(laser.rect.x)
            nearest_y = self.round_to_nearest_tile(laser.rect.y)

            tile = self.level.get_tile_from_object_layer(nearest_x, nearest_y)

            if tile:
                tile = tile[0]
                if isinstance(tile, SolidTile):
                    break

            self.lasers.add(laser)

        if len(self.lasers) > self.range:
            self.level.sprites.remove(self.lasers)
            self.lasers.empty()
        self.level.sprites.add(self.lasers)

    def handle_collision(self, tile, player, level):
        # TODO - needs to be pixel perfect - Use masks.
        if pygame.sprite.spritecollide(player, self.lasers, False):
            pygame.sprite.Sprite.kill(player)

        heading = self.target - self.position
        distance = heading.length()

        if heading != [0,0]:
            heading.normalize_ip()

        if distance <= 2:  # We're closer than 2 pixels.
            self.waypoint_index = (self.waypoint_index + 1) % len(self.path.points)
            self.target = self.path.points[self.waypoint_index]

        self.vel = heading * self.speed
        self.position += self.vel
        self.rect.topleft = self.position

        self.pin_laser()

    def pin_laser(self):
        for laser in self.lasers:
            laser.rect.x = self.rect.centerx - 2 # laser's width
            # laser.rect.y = self.rect.y


# For now just do "up"
class Line(Entity):

    def __init__(self, x, y, width, height, image=None):
        Entity.__init__(self, x, y, width, height, image)
        self.image = pygame.Surface((width, height))
        self.image.fill((255,0,0))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
        self.timer = 1

    def update(self, delta_time):
        self.timer -= delta_time

        if self.timer <=0:
            self.image.fill(
                (
                random.randint(0,255), 
                random.randint(0,255), 
                random.randint(0,255), 
                )
            )
            self.timer = 1

