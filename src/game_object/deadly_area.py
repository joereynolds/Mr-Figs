
import pygame

from src.game_object.switch_tile import Switch
import src.game_object.tile as tile
import src.entity as entity
import src.colours as colours
import src.graphics as graphics

class DeadlyArea(entity.Entity):
    """
    An area that kills the player if collided with
    """
    def __init__(self, x, y, width, height, image):
        entity.Entity.__init__(self, x, y, width, height)
