"""
This is the thing that mr-figs can stand on and
be moved around on.
"""

import pygame
import src.interpolate as interpolate
from src.game_object.path import Path
import src.entity as entity
import src.colours as colours
import src.graphics as graphics
import time

class Platform(entity.Entity):
    # TODO - Typehint path as Path
    def __init__(self, x, y, width, height, follows_path_id=None, path=None, image=None, ):
        entity.Entity.__init__(self, x, y, width, height, image)
        self.minimap_colour = colours.RED_HIGHLIGHT
        self.follows_path_id = follows_path_id
        self.path = path
        self.speed =  graphics.tile_width // 2
        self.player_on_platform = False
        self.processed_points = []

    def move_to(self, target_x, target_y, player):
        """Checks to see if we've reached the destination given, if we have,
        we can stop moving. Note that we need to use delta-time otherwise we'll get
        schmancy interpolation effects"""

        if target_x < self.rect.x:
            self.rect.x -= self.speed
        elif target_x > self.rect.x:
            self.rect.x += self.speed
        elif target_y < self.rect.y:
            self.rect.y -= self.speed
        elif target_y > self.rect.y:
            self.rect.y += self.speed

        if self.rect.x == target_x and self.rect.y == target_y:
            self.processed_points.append((target_x, target_y))

    def has_reached_to_destination(self):
        return self.rect.x == self.path.points[-1][0] and self.rect.y == self.path.points[-1][1]

    def handle_collision(self, tile, player, level):
        if self.has_reached_to_destination():
            self.processed_points = []

        if player.destination[0] == self.rect.x and player.destination[1] == self.rect.y:
            self.player_on_platform = True
            # This is horrible, we shouldn't have to manually set this stuff
            player.rect.x = self.rect.x
            player.rect.y = self.rect.y
            player.moving = False

        if self.player_on_platform and not self.has_reached_to_destination():
            for point in self.path.points:
                if point not in self.processed_points:
                    self.move_to(point[0], point[1], player)
                    player.destination[0] = point[0]
                    player.destination[1] = point[1]
