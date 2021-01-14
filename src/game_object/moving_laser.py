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
import src.movement_vector as movement_vector

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
            direction: str,
            speed: int = 2,
            image=None,
        ):
        Entity.__init__(self, x, y, width, height, image)
        self.minimap_colour = colours.RED_HIGHLIGHT
        self.path = path
        self.direction = direction
        self.destination = path.points[-1]
        self.position = Vector2(x, y)
        self.vel = Vector2(0, 0)
        self.target = self.path.points[1]
        self.target_radius = 25
        self.speed = speed
        self.waypoint_index = 0
        self.level = level
        self.lasers = pygame.sprite.LayeredUpdates()
        self.laser_thickness = 2
        self.speed = 0.5

        self.horizontal_laser_range = min(self.level._map.width, 25)
        self.vertical_laser_range = min(self.level._map.height, 25)

        self.screen_width, self.screen_height = pygame.display.get_window_size()
        self.range = self.vertical_laser_range
        if self.direction in ['left', 'right']:
            self.range = self.horizontal_laser_range

    def round_to_nearest_tile(self, x, base = graphics.tile_width):
        return base * round(x/base)

    def update(self, delta_time):

        for i in range(self.range):
            if self.direction == 'up':
                next_tile_y = self.rect.y - (i * graphics.tile_height)

                if next_tile_y < self.screen_height and next_tile_y > 0:
                    laser = Line(
                        self.rect.x, 
                        next_tile_y,
                        self.laser_thickness, 
                        graphics.tile_height
                    )

            if self.direction == 'right':
                next_tile_x = self.rect.x + (i * graphics.tile_width)

                if next_tile_x > 0 and next_tile_x < self.screen_width:
                    laser = Line(
                        next_tile_x, 
                        self.rect.centery,
                        graphics.tile_height,
                        self.laser_thickness, 
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

        for bomb in player.bombs:
            if pygame.sprite.spritecollide(bomb, self.lasers, False):
                bomb.explode()
                # TODO - currently we can't see the particles because
                # it happens so fast. Set this on a timer
                pygame.sprite.Sprite.kill(bomb)

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
            if self.direction == 'up':
                laser.rect.x = self.rect.centerx - self.laser_thickness
            if self.direction == 'right':
                laser.rect.y = self.rect.centery - self.laser_thickness

    def get_vector_for_direction(self, direction):
        return movement_vector.vector[direction]

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

        if self.timer <= 0:
            # do something cool, maybe pulse?
            self.timer = 1
