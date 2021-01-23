"""
Renders out a visual of how many bombs are in our inventory
"""
import pygame

from src.gui.text_element import TextElement
from src.entity import Entity
from src.game_object.actor import Actor
from src.resolution_asset_sizer import ResolutionAssetSizer
import src.graphics as graphics
import src.colours as colours
import src.config as config

class BombDisplay(Entity):

    def __init__(self, x: int, y: int, width: int, height: int, image=None):
        Entity.__init__(self, x, y, width, height, image)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.asset_sizer = ResolutionAssetSizer()
        self.font_size = self.asset_sizer.get_font_size(
            pygame.display.get_window_size()
        )

        self.surface = pygame.Surface((width, height)).convert_alpha()
        self.bomb_image = graphics.sprites['bomb']['sprites'][0],
        self.bomb_image = self.bomb_image[0]

        self.bomb_image_width_scaled = round(self.bomb_image.get_width() * 4)
        self.bomb_image_height_scaled = round(self.bomb_image.get_height() * 4)

        self.scaled_bomb_image = pygame.transform.scale(
            self.bomb_image,
            (self.bomb_image_width_scaled, self.bomb_image_height_scaled)
        )

    def render(self, bomb_count):
        """Renders text at the default position of (0,0) or otherwise
        if a position is supplied.
        @position = Position for the text to be rendered (optional)
        """
        self.surface.fill((0,0,0, 0))
        for i in range(bomb_count):
            self.surface.blit(
                self.scaled_bomb_image,
                ((i + 1) * self.bomb_image.get_width(), 64)
            )
