import pygame

import src.graphics as graphics
import src.config as config
import src.colours as colours
import src.scenes.scenebase as scene_base
from src.input_handlers.options_input_handler import OptionsInputHandler
from src.gui.clickable import Clickable
from src.gui.checkbox import Checkbox
from src.resolution_asset_sizer import ResolutionAssetSizer

class OptionsMenu(scene_base.SceneBase):
    """Options menu for toggling music etc..."""

    def __init__(self):
        scene_base.SceneBase.__init__(
            self,
            OptionsInputHandler(self)
        )
        self.components = pygame.sprite.LayeredUpdates()
        asset_sizer = ResolutionAssetSizer()
        size = pygame.display.get_window_size()
        width = size[0]
        height = size[1]
        self.image = pygame.image.load('./data/background-scene.png').convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        center_x = width // 2

        offset = asset_sizer.get_button_offset(size)
        spacing = asset_sizer.get_button_spacing(size)
        button_width = width // 4
        button_height = height // 12
        checkbox_width = graphics.tile_width * graphics.ZOOM_LEVEL

        self.music_toggle_text = "[T]OGGLE MUSIC"
        self.font_size = asset_sizer.get_font_size(size)
        self.font = pygame.font.Font(config.font, self.font_size)
        self.menu_items = {
            'toggle_music': pygame.sprite.GroupSingle(Checkbox(offset, offset, checkbox_width, button_height, 0)),
            'clear_data': pygame.sprite.GroupSingle(Clickable(offset, offset + (button_height * 1) + (spacing * 1), button_width, button_height, '[C]LEAR GAME DATA')),
            'go_back': pygame.sprite.GroupSingle(Clickable(offset, offset + (button_height * 2) + (spacing * 2), button_width, button_height, '[B]ACK'))
        }

    def render(self):
        """Fill our surface and render our buttons"""
        self.surface.blit(self.image, ((0,0)))

        rendered_text = self.font.render(
            self.music_toggle_text, 
            False, 
            colours.GREEN_HIGHLIGHT
        )

        self.surface.blit(
            rendered_text, 
            (
                self.menu_items['toggle_music'].sprite.rect.right + 25, 
                self.menu_items['toggle_music'].sprite.rect.top, 
            )
        )

        self.menu_items['toggle_music'].draw(self.surface)
        self.menu_items['clear_data'].draw(self.surface)
        self.menu_items['go_back'].draw(self.surface)
        self.menu_items['toggle_music'].sprite.render()
        self.menu_items['clear_data'].sprite.render()
        self.menu_items['go_back'].sprite.render()
