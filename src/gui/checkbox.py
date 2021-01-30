import pygame
from src.gui.clickable import Clickable
import src.colours as colours
import src.graphics as g
import src.config as config
from src.resolution_asset_sizer import ResolutionAssetSizer

sprites = {
    0: g.subsurf(g.grid(8,5)),
    1: g.subsurf(g.grid(7,5)),
}
    
class Checkbox(Clickable):

    def __init__(self, x, y, width, height, state, name, string="TOGGLE MUSIC"):
        Clickable.__init__(self, x, y, width, height, string=string)
        self.state = state
        self.name = name
        self.width = width
        self.height = height

        asset_sizer = ResolutionAssetSizer()
        size = pygame.display.get_window_size()
        self.scale_to = asset_sizer.get_button_size(size)

        self.image = g.spritesheet.subsurface(
                0 * g.tile_width, 
                9 * g.tile_height, 
                g.tile_width * 3, 
                g.tile_height
        )

        self.selected_image = g.spritesheet.subsurface(
            0 * g.tile_width, 
            10 * g.tile_height, 
            g.tile_width * 3, 
            g.tile_height
        )
        self.selected_image = pygame.transform.scale(self.selected_image, (self.width, self.height))

        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.image_rect = self.image.get_rect()

        self.checkbox_image = sprites[self.state]
        self.checkbox_image = pygame.transform.scale(
            self.checkbox_image, 
            self.scale_to
        )
        self.checkbox_image_rect = self.checkbox_image.get_rect()

        self.text = string
        self.font_size = asset_sizer.get_font_size(size)
        self.font = pygame.font.Font(config.font, self.font_size)

    def toggle(self, function, *args):
        self.state = not self.state

        self.checkbox_image = sprites[self.state]
        self.checkbox_image = pygame.transform.scale(self.checkbox_image, self.scale_to)

        function(*args)

    def render(self):
        rendered_text = self.font.render(self.text, False, colours.WHITE)

        self.image.blit(
            self.checkbox_image, 
            (
                self.image_rect.left + 25,
                self.image_rect.centery - 50
            )
        )

        self.image.blit(
            rendered_text, 
            (
                self.checkbox_image_rect.right,
                self.image_rect.centery - 50
            )
        )
