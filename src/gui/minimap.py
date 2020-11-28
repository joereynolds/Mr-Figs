"""
Renders out a minimap of the game.
"""
import pygame

from src.entity import Entity
import src.colours as colours
import src.config as config

class Minimap(Entity):

    # PRetty sure that although this is used,
    # it's pointless
    HEIGHT = 84

    SPRITE_WIDTH = 8
    SPRITE_HEIGHT = 8

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
        """
        self.map.empty()
        for sprite in self.tiled_level.sprites:
            minimap_sprite = Entity(
                self.rect.x + sprite.rect.x / 2,
                self.rect.y + sprite.rect.y / 2,
                Minimap.SPRITE_WIDTH,
                Minimap.SPRITE_HEIGHT,
            )
            minimap_sprite.image.fill(sprite.minimap_colour)

            self.map.add(minimap_sprite)

    def render(self):
        self.populate_map()
        self.map.draw(self.surface)
