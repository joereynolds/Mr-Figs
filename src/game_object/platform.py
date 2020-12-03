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
    def __init__(
            self, 
            x: int, 
            y: int, 
            width: int, 
            height: int, 
            follows_path_id=None, 
            path=None, 
            image=None
        ):
        entity.Entity.__init__(self, x, y, width, height, image)
        self.minimap_colour = colours.RED_HIGHLIGHT
        self.follows_path_id = follows_path_id
        self.path = path
        self.speed =  2
        self.player_on_platform = False
        self.processed_points = []

        # Note that there's a self.destination but that is set after the fact
        # inside level editor, messy I know. Would be good to refactor somehow

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

        player.rect.x = self.rect.x
        player.rect.y = self.rect.y
        player.destination[0] = self.rect.x
        player.destination[1] = self.rect.y

        if self.rect.x == target_x and self.rect.y == target_y:
            self.processed_points.append((target_x, target_y))

    def has_reached_destination(self):
        return self.rect.x == self.destination[0] and self.rect.y == self.destination[1]

    def toggle_destination(self):
        """
        When we arrive at our TO destination, if we get back on
        the platform, we want to be taken to our FROM destination.
        """
        if self.destination == self.path.points[-1]:
            self.destination = self.path.points[0]

    def handle_collision(self, tile, player, level):
        if self.has_reached_destination() and not self.player_on_platform:
            self.processed_points = []
            self.toggle_destination()

        if player.destination[0] == self.rect.x and player.destination[1] == self.rect.y:
            self.player_on_platform = True
            player.moving = False
        else: 
            self.player_on_platform = False

        if self.player_on_platform and not self.has_reached_destination():
            for point in self.path.points:
                if point not in self.processed_points:
                    self.move_to(point[0], point[1], player)
