"""
Renders out a visual of how many bombs are in our inventory
"""
import pygame

from src.entity import Entity
from src.resolution_asset_sizer import ResolutionAssetSizer
import src.graphics as graphics

class BombDisplay(Entity):

    def __init__(self, x: int, y: int, width: int, height: int, image=None):
        Entity.__init__(self, x, y, width, height, image)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.asset_sizer = ResolutionAssetSizer()
        self.size = pygame.display.get_window_size()

        self.tile_size = self.asset_sizer.get_button_size(self.size)
        self.font_size = self.asset_sizer.get_font_size(self.size)

        self.surface = pygame.Surface((width, height)).convert_alpha()
        self.bomb_image = graphics.sprites['bomb']['sprites'][0],
        self.bomb_image = self.bomb_image[0]

        self.scaled_bomb_image = pygame.transform.scale(
            self.bomb_image,
            (self.tile_size[0], self.tile_size[1])
        )

    def render(self, bomb_count):
        self.surface.fill((0,0,0, 0))
        for i in range(bomb_count):
            self.surface.blit(
                self.scaled_bomb_image,
                ((i + 1) * self.bomb_image.get_width(), 64)
            )
