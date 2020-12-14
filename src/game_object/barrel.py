import pygame
import src.colours as colours
from src.game_object.bullet import Bullet
from src.entity import Entity
import src.movement_vector as movement_vector

class Barrel(Entity):

    def __init__(self, x, y, width, height, direction, image=None):
        Entity.__init__(self, x, y, width, height, image)
        self.minimap_colour = colours.WHITE
        self.direction = direction
        self.vector = self.get_vector_for_direction(self.direction)

    def shoot(self, level):
        bullet = Bullet(self.rect.x, self.rect.y, 5, 5, self.direction)
        level.sprites.add(bullet)
        print("bang to the ", self.direction)

    def get_vector_for_direction(self, direction):
        return movement_vector.vector[direction]
