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

    def __init__(self, x, y, width, height, level, image=None):
        """
        @level     = level data from the LevelEditor class
        """
        Entity.__init__(self, x, y, width, height, image)


        self.x = x
        self.y = y
        self.level= level
        self.height = height
        self.is_visible = False
        self.width = self.level.tiled_level._map.width * graphics.tile_width
        self.height = self.level.tiled_level._map.height * graphics.tile_height

        self.map = pygame.sprite.Group()
        asset_sizer = ResolutionAssetSizer()
        self.size_data = asset_sizer.get_minimap_sprite_size(pygame.display.get_window_size())
        self.populate_map()
        self.surface = pygame.Surface((self.width, self.height)).convert_alpha()

    def toggle_visiblity(self):
        self.is_visible = not self.is_visible

    def close_menu(self):
        self.is_visible = False

    def populate_map(self):
        """
        Populates a minimap i.e. A smaller representation of the game itself.
        """
        self.map.empty()
        for sprite in self.level.sprites:
            minimap_sprite = Entity(
                sprite.rect.x,
                sprite.rect.y,
                graphics.tile_width,
                graphics.tile_height
            )

            if hasattr(sprite, 'minimap_colour'):
                minimap_sprite.image.fill(sprite.minimap_colour)

                self.map.add(minimap_sprite)

    def render(self, game_surface):
        self.surface.fill((5, 5, 5, 200))
        self.populate_map()
        self.map.draw(self.surface)
        game_surface.blit(self.surface, (self.x ,self.y))
