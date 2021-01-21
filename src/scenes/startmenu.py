import pygame

import src.graphics as graphics
import src.colours as colours
import src.scenes.scenebase as scene_base
import src.input_handlers.start_menu_input_handler as input_handler
from src.gui.clickable import Clickable
from src.gui.menu_items import MenuItems
from src.resolution_asset_sizer import ResolutionAssetSizer

class StartMenu(scene_base.SceneBase):
    """Initial start menu at the start of the game"""

    def __init__(self):
        scene_base.SceneBase.__init__(
            self,
            input_handler.StartMenuInput(self),
            graphics.get_controller()
        )
        self.components = pygame.sprite.LayeredUpdates()
        size = pygame.display.get_window_size()
        width = size[0]
        height = size[1]
        self.image = pygame.image.load('./data/mr-figs-title-draft.png').convert()
        self.image = pygame.transform.scale(self.image, (size[0], size[1]))
        self.rect = self.image.get_rect()

        asset_sizer = ResolutionAssetSizer()

        button_width, button_height = asset_sizer.get_button_size(size)
        button_width *= 8
        button_height *= 2

        offset = button_height

        bottom = self.rect.bottom

        items = {
            'start-button': pygame.sprite.GroupSingle(
                Clickable(
                    self.rect.left, 
                    bottom - offset * 3,
                    button_width, 
                    button_height, 
                    string='[S]TART GAME', 
                    selected=True,
                    name="introduction"
                    )
                ),
            'options': pygame.sprite.GroupSingle(
                Clickable(
                    self.rect.left, 
                    bottom - offset * 2, 
                    button_width, 
                    button_height, 
                    string='[O]PTIONS',
                    name="options-menu"
                    )
                ),
            'quit': pygame.sprite.GroupSingle(
                Clickable(
                    self.rect.left, 
                    bottom - offset, 
                    button_width, 
                    button_height, 
                    string='[Q]UIT',
                    name="quit"
                    )
                )
        }

        self.menu_items = MenuItems(items)

    def render(self):
        """Fill our surface and render our buttons"""
        
        self.surface.blit(self.image, ((0,0)))
        self.menu_items.items['start-button'].draw(self.surface)
        self.menu_items.items['start-button'].sprite.render()
        self.menu_items.items['options'].draw(self.surface)
        self.menu_items.items['options'].sprite.render()
        self.menu_items.items['quit'].draw(self.surface)
        self.menu_items.items['quit'].sprite.render()
