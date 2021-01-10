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
        self.image = pygame.image.load('./data/background-scene.png').convert()

        size = pygame.display.get_window_size()
        width = size[0]
        height = size[1]
        asset_sizer = ResolutionAssetSizer()

        asset_sizer.get_nearest_available_resolution(size)

        offset = asset_sizer.get_button_offset(size)
        spacing = asset_sizer.get_button_spacing(size)
        button_width = width // 4
        button_height = graphics.round_to_nearest_tile(height // graphics.tile_height * 1.5)

        self.image = pygame.transform.scale(self.image, (size[0], size[1]))

        items = {
            'start-button': pygame.sprite.GroupSingle(
                Clickable(
                    offset, 
                    offset, 
                    button_width, 
                    button_height, 
                    '[S]TART GAME', 
                    True,
                    name="introduction"
                    )
                ),
            'options': pygame.sprite.GroupSingle(
                Clickable(
                    offset, 
                    offset + (button_height * 1) + (spacing * 1), 
                    button_width, 
                    button_height, 
                    '[O]PTIONS',
                    name="options-menu"
                    )
                ),
            'quit': pygame.sprite.GroupSingle(
                Clickable(
                    offset, 
                    offset + (button_height * 2) + (spacing * 2), 
                    button_width, 
                    button_height, 
                    '[Q]UIT',
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
