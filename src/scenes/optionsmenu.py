import pygame

import src.graphics as graphics
import src.config as config
import src.colours as colours
import src.scenes.scenebase as scene_base
from src.gui.menu_items import MenuItems
from src.input_handlers.options_input_handler import OptionsInputHandler
from src.gui.clickable import Clickable
from src.gui.checkbox import Checkbox
from src.resolution_asset_sizer import ResolutionAssetSizer

class OptionsMenu(scene_base.SceneBase):
    """Options menu for toggling music etc..."""

    def __init__(self):
        scene_base.SceneBase.__init__(
            self,
            OptionsInputHandler(self),
            graphics.get_controller()
        )
        self.components = pygame.sprite.LayeredUpdates()
        asset_sizer = ResolutionAssetSizer()
        size = pygame.display.get_window_size()
        self.image = pygame.image.load(config.image_dir + 'mr-figs-title-draft.png').convert()
        self.image = pygame.transform.scale(self.image, (size[0], size[1]))
        self.rect = self.image.get_rect()

        button_width, button_height = asset_sizer.get_button_size(size)

        left = self.rect.left + button_width

        button_width *= 6
        button_height *= 2

        offset = button_height
        bottom = self.rect.bottom

        checkbox_width = asset_sizer.get_button_size(size)[0]

        self.music_toggle_text = "[T]OGGLE MUSIC"
        self.font_size = asset_sizer.get_font_size(size)
        self.font = pygame.font.Font(config.font, self.font_size)

        items = {
            'toggle_music': pygame.sprite.GroupSingle(
                Checkbox(
                    left, 
                    bottom - offset * 3, 
                    checkbox_width, 
                    button_height, 
                    0, 
                    name='toggle_music'
                    )
                ),
            'clear_data': pygame.sprite.GroupSingle(
                Clickable(
                    left, 
                    bottom - offset * 2,
                    button_width, 
                    button_height, 
                    string='CLEAR GAME DATA', 
                    name='clear_data')),
            'go_back': pygame.sprite.GroupSingle(
                Clickable(
                    left, 
                    bottom - offset,
                    button_width, 
                    button_height, 
                    string='BACK', 
                    selected=True,
                    name='go_back'
                )
            )
        }

        self.menu_items = MenuItems(items, selected_index=2)

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
                self.menu_items.items['toggle_music'].sprite.rect.right + 25, 
                self.menu_items.items['toggle_music'].sprite.rect.top, 
            )
        )

        self.menu_items.update()
        self.menu_items.items['toggle_music'].draw(self.surface)
        self.menu_items.items['clear_data'].draw(self.surface)
        self.menu_items.items['go_back'].draw(self.surface)
        self.menu_items.items['toggle_music'].sprite.render()
        self.menu_items.items['clear_data'].sprite.render()
        self.menu_items.items['go_back'].sprite.render()
