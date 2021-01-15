import pygame
import src.colours as colours
import src.entity as entity

class SolidTile(entity.Entity):
    """The tile class represents any tile in the game background,
        or foreground.
        It extends the entity class
        to add collision mechanics and various other bits"""

    def __init__(self, x, y, width, height, image=None):
        entity.Entity.__init__(self, x, y, width, height, image)
        self.solid = True
        self.minimap_colour = colours.GREEN_BASE

    def handle_pre_bomb_particle_creation(self, level):
        return False
