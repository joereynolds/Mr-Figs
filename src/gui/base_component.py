import pygame
import src.gui.text_element as text_element
from src.resolution_asset_sizer import ResolutionAssetSizer
import src.config as config
import src.graphics as graphics


class BaseComponent(pygame.sprite.Sprite):

    def __init__(
            self, 
            x, 
            y, 
            width, 
            height, 
            image=graphics.button_image,
            string='Default', 
            selected=False, 
            name="Default"
        ):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = image
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

        self.default_image = graphics.spritesheet.subsurface(
            0 * graphics.tile_width, 
            9 * graphics.tile_height, 
            graphics.tile_width * 3, 
            graphics.tile_height
        )

        # TODO - need more intelligent resizing here
        self.default_image = pygame.transform.scale(
            self.default_image,
            (graphics.tile_width * 24, graphics.tile_height * 8)
        )

        self.selected_image = graphics.spritesheet.subsurface(
            0 * graphics.tile_width, 
            10 * graphics.tile_height, 
            graphics.tile_width * 3, 
            graphics.tile_height
        )

        self.selected_image = pygame.transform.scale(
            self.selected_image,
            (graphics.tile_width * 24, graphics.tile_height * 8)
        )

        self.default_image = self.default_image.convert_alpha()
        self.selected_image = self.selected_image.convert_alpha()


    def on_selected(self, func, *args):
        """When we've selected the item, do these things"""
        func(*args)

    def render(self, position=False):
        """A wrapper to encapsulate all rendering"""

        if self.selected:
            self.image = self.selected_image
        else: self.image = self.default_image

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
