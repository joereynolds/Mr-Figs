"""
An enemy that follows a pre-determined path
and also plants bombs
"""

from src.game_object.bomb import Bomb
import pygame
from pygame.math import Vector2
import src.interpolate as interpolate
from src.game_object.path import Path
import src.entity as entity
import src.colours as colours
import src.graphics as graphics
import time

class EnemyBombable(entity.Entity):
    def __init__(
            self, 
            x: int, 
            y: int, 
            width: int, 
            height: int, 
            path: Path, 
            image=None
        ):
        entity.Entity.__init__(self, x, y, width, height, image)
        self.minimap_colour = colours.RED_HIGHLIGHT
        self.path = path
        self.position = Vector2(x, y)
        self.vel = Vector2(0, 0)
        self.target = self.path.points[1]
        self.max_speed = 1
        self.waypoint_index = 0
        self.bomb_timer = 100

    def handle_collision(self, tile, player, level):
        if pygame.sprite.collide_rect(self, player.collideable):
            pygame.sprite.Sprite.kill(player)

        heading = self.target - self.position
        distance = heading.length()

        if heading != [0,0]:
            heading.normalize_ip()

        if distance <= 1:  # We're closer than a pixel
            self.waypoint_index = (self.waypoint_index + 1) % len(self.path.points)
            self.target = self.path.points[self.waypoint_index]

        can_plant = True

        if self.rect.x % graphics.tile_width == 0 and self.rect.y % graphics.tile_height == 0:
            if self.bomb_timer < 0:
                for bomb in level.player.bombs:
                    if self.rect.x == bomb.rect.x and self.rect.y == bomb.rect.y:
                        can_plant = False

                if can_plant:
                    player.bombs.add(Bomb(
                        self.rect.x,
                        self.rect.y,
                        graphics.tile_width,
                        graphics.tile_height,
                        level.tiled_level,
                        5,
                        graphics.sprites['bomb']['sprites'][0]
                    ))
                self.bomb_timer = 100
        self.bomb_timer -= 1

        self.vel = heading * self.max_speed # Otherwise move with max_speed.
        self.position += self.vel
        self.rect.topleft = self.position
