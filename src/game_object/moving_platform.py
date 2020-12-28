"""
This is the thing that mr-figs can stand on and
be moved around on.
"""

import pygame
from pygame.math import Vector2
from src.game_object.path import Path
import src.entity as entity
import src.colours as colours
import src.graphics as graphics

class MovingPlatform(entity.Entity):
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
        self.max_speed = 1
        self.position = Vector2(x, y)
        self.waypoint_index = 0
        self.vel = Vector2(0, 0)
        self.target = self.path.points[1]
        self.timer = 50

    def pin_player(self, player, x, y):
        """
        Pins the player to x and y.
        Otherwise they wouldn't move
        """
        player.rect.x = x
        player.rect.y = y
        player.destination[0] = x
        player.destination[1] = y

    def handle_collision(self, tile, player, level):
        self.timer -= 1

        if self.timer <= 0:
            if pygame.sprite.collide_rect(self, player):
                self.pin_player(player, self.position.x, self.position.y)

            heading = self.target - self.position
            distance = heading.length()

            if heading != [0,0]:
                heading.normalize_ip()

            if distance <= 1:  # We're closer than 2 pixels.
                self.waypoint_index = (self.waypoint_index + 1) % len(self.path.points)
                self.target = self.path.points[self.waypoint_index]

            self.vel = heading * self.max_speed
            self.position += self.vel
            self.rect.topleft = self.position

            if self.rect.x % 16 == 0:
                self.timer = 50
