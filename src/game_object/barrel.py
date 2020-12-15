import pygame
import src.colours as colours
from src.game_object.bullet import Bullet
from src.entity import Entity
import src.movement_vector as movement_vector

class Barrel(Entity):

    def __init__(self, x, y, width, height, direction, level, image=None):
        Entity.__init__(self, x, y, width, height, image)
        self.minimap_colour = colours.WHITE
        self.direction = direction
        self.vector = self.get_vector_for_direction(self.direction)
        self.level = level

        self.bullet_timer = 1
        self.burst_fire_timer = 0.1


    def update(self, delta_time):
        self.bullet_timer-= delta_time

        if self.bullet_timer <= 0:
            bullet = Bullet(self.rect.centerx, self.rect.centery, 2, 2, self.direction)
            self.level.sprites.add(bullet)
            self.bullet_timer = 1

    def get_vector_for_direction(self, direction):
        return movement_vector.vector[direction]
