import pygame
import src.gui.text_element as text_element
from src.resolution_asset_sizer import ResolutionAssetSizer
import src.config as config


class BaseComponent(pygame.sprite.Sprite):

    def __init__(
            self, 
            x, 
            y, 
            width, 
            height, 
            string='Default', 
            selected=False, 
            name="Default"
        ):
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
        self.selected = selected
        self.name = name
        self.font = pygame.font.Font(config.font, self.font_size)

    def on_selected(self, func, *args):
        """When we've selected the item, do these things"""
        func(*args)

    def render(self, position=False):
        """A wrapper to encapsulate all rendering"""

        if self.selected:
            self.image.fill((255,255,255))
        else: self.image.fill((0,0,0))

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

        rendered_text = self.font.render(self.text.text.upper(), False, self.text.color)
        self.image.blit(rendered_text, self.text.position)
