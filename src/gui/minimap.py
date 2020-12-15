"""
Renders out a minimap of the game.
"""
import pygame

from src.entity import Entity
from src.resolution_asset_sizer import ResolutionAssetSizer
import src.graphics as graphics
import src.colours as colours
import src.config as config

class Minimap(Entity):

    # PRetty sure that although this is used,
    # it's pointless
    HEIGHT = 84

    def __init__(self, x, y, width, height, level, image=None):
        """
        @level     = level data from the LevelEditor class
        """
        Entity.__init__(self, x, y, width, height, image)

        self.tiled_level = level
        self.map = pygame.sprite.Group()
        asset_sizer = ResolutionAssetSizer()
        self.size_data = asset_sizer.get_minimap_sprite_size(pygame.display.get_window_size())
        self.populate_map()
        self.minimap_colour = colours.RED_GLOW
        self.surface = pygame.Surface((200, 200)).convert_alpha()

    def populate_map(self):
        """
        Populates a minimap i.e. A smaller representation of the game itself.
        """
        self.map.empty()
        for sprite in self.tiled_level.sprites:
            minimap_sprite = Entity(
                sprite.rect.x * self.size_data['sprite_placement_modifier'],
                sprite.rect.y * self.size_data['sprite_placement_modifier'],
                self.size_data['width'],
                self.size_data['height']
            )

            if hasattr(sprite, 'minimap_colour'):
                minimap_sprite.image.fill(sprite.minimap_colour)

                self.map.add(minimap_sprite)

    def render(self):
        self.surface.fill((0,0,0,200))
        self.populate_map()
        self.map.draw(self.surface)
