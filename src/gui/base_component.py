import pygame
import src.gui.text_element as text_element
from src.resolution_asset_sizer import ResolutionAssetSizer
import src.config as config


class BaseComponent(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, string='Default'):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.text = text_element.TextElement(text=string)
        self.asset_sizer = ResolutionAssetSizer()
        self.font_size = self.asset_sizer.get_font_size(
            pygame.display.get_window_size()
        )

    def render(self, position=False):
        """A wrapper to encapsulate all rendering"""
        self.render_text(position)

    def render_text(self, position=False, color=False):
        """Renders text at the default position of (0,0) or otherwise
        if a position is supplied.
        @position = Position for the text to be rendered (optional)
        """
        self.text.position = (0, 0)
        if position:
            self.text.position = position

        if color:
            self.text.set_color(color)

        font_object = pygame.font.Font(config.font, self.font_size)
        rendered_text = font_object.render(self.text.text.upper(), False, self.text.color)
        self.image.blit(rendered_text, self.text.position)
