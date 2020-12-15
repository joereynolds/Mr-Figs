import pygame
import src.colours as colours
from src.entity import Entity
from pygame.math import Vector2

class Particle(Entity):

    def __init__(self, pos: Vector2, width, height, ttl, colour):
        Entity.__init__(self, pos.x, pos.y, width, height, None)
        # Not sure why we need to manually set pygame's layer?
        # even calling move_to_front didn't work.
        self._layer = 1
        self.pos = pos
        self.image = pygame.Surface((width, height)).convert_alpha()
        self.image.fill(colour)
        self.ttl = ttl

    def update(self, dt):
        self.ttl -= 1
