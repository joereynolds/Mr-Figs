"""
Renders out a minimap of the game.
Currently this does very little.
At the moment just a red square is overlayed with some transparency.
"""
import pygame

from src.entity import Entity
from src.actor import Actor
import src.colours as colours
import src.config as config

class Minimap(Entity):

    WIDTH = config.screen_width / 8
    HEIGHT = config.screen_height / 8

    SPRITE_WIDTH = 50
    SPRITE_HEIGHT = 50

    def __init__(self, x, y, width, height, level, surface, image=None):
        """
        @level     = level data from the LevelEditor class
        """
        Entity.__init__(self, x, y, width, height, image)
        self.image.fill(colours.RED_GLOW)
        self.image.set_alpha(50)

        self.tiled_level = level
        self.surface = surface
        self.map = pygame.sprite.Group()
        self.populate_map()
        self.minimap_colour = colours.RED_GLOW
    
    def populate_map(self):
        """
        Populates a minimap i.e. A smaller representation of the game itself.
        Note the magic number '6'. This is just 48 (the size of our sprites) divided by 8
        (A number that looked good enough)
        """
        self.map.empty()
        for sprite in self.tiled_level.sprites:
            minimap_sprite = Entity(
                self.rect.x + sprite.rect.x / 8,
                self.rect.y + sprite.rect.y / 8,
                6,
                6
            )
            minimap_sprite.image.fill(sprite.minimap_colour)

            self.map.add(minimap_sprite)

    def render(self):
        self.populate_map()
        self.map.draw(self.surface)
