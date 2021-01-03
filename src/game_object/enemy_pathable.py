"""
An enemy that follows a pre-determined path
"""

import pygame
from pygame.math import Vector2
import src.interpolate as interpolate
from src.game_object.path import Path
import src.entity as entity
import src.colours as colours
import src.graphics as graphics
import time

class EnemyPathable(entity.Entity):
    """Represents most things that follow a path and kill you.
    Not just literal enemies, could also be saw blades etc..."""
    def __init__(
            self, 
            x: int, 
            y: int, 
            width: int, 
            height: int, 
            path: Path, 
            speed: int = 2,
            image=None
        ):
        entity.Entity.__init__(self, x, y, width, height, image)
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

    def handle_collision(self, tile, player, level):
        if pygame.sprite.collide_rect(self, player):
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
