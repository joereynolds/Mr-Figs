"""
Renders out a minimap of the game.
Currently this does very little. 
At the moment just a red square is overlayed with some transparency.
"""
import pygame

import src.config as config
from src.entity import Entity
from src.actor import Actor
import src.colours as colours

class Minimap(Entity):

    HEIGHT = 250
    WIDTH = 250
    """
    @level     = level data from the LevelEditor class
    """
    def __init__(self, x, y, width, height, level, image=None):
        Entity.__init__(self, x, y, width, height, image)
        self.image.fill(colours.RED_GLOW)
        self.image.set_alpha(50)

        self.tiled_level = level
        self.map = pygame.sprite.Group()
        self.populate_map()

    def populate_map(self):
        for sprite in self.tiled_level.sprites:
            if (isinstance(sprite, Actor)):
                sprite = Entity(
                        config.screen_width - 5, 
                        sprite.rect.y, 
                        50, 
                        50
                )
                sprite.image.fill(colours.BLUE_HIGHLIGHT)

            self.map.add(sprite)
