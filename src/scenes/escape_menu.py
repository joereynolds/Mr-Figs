import pygame
import src.graphics as graphics
import src.colours as colours
import src.config as config
import src.scenes.scenebase as scene_base
import src.input_handlers.escape_menu_input_handler as input_handler
from src.gui.clickable import Clickable
from src.gui.menu_items import MenuItems
from src.resolution_asset_sizer import ResolutionAssetSizer

class EscapeMenu(scene_base.SceneBase):
    """The menu that pops up during game when we press escape"""

    def __init__(self):
        scene_base.SceneBase.__init__(
            self, 
            input_handler.EscapeMenuInput(self),
            graphics.get_controller()
        ) 

        self.is_visible = False
        self.width, self.height = pygame.display.get_window_size()

        self.surface = pygame.Surface((self.width // 2, self.height - 64)).convert_alpha()
        asset_sizer = ResolutionAssetSizer()

        size = pygame.display.get_window_size()
        button_x = self.surface.get_width() // 4
        button_width = self.surface.get_width() // 2
        button_height = asset_sizer.get_button_height(size)
        button_offset = button_height

        items = {
            'continue': pygame.sprite.GroupSingle(
                Clickable(
                    button_x, 
                    button_offset, 
                    button_width, 
                    button_height, 
                    string='[C]ontinue', 
                    selected=True, 
                    name='continue'
                )
            ),

            'restart': pygame.sprite.GroupSingle(
                Clickable(
                    button_x, 
                    button_offset * 3, 
                    button_width, 
                    button_height, 
                    string='[R]estart', 
                    name='restart'
                )
            ),

            'quit_to_main': pygame.sprite.GroupSingle(
                Clickable(
                    button_x, 
                    button_offset * 5, 
                    button_width, 
                    button_height, 
                    string='[Q]uit to main menu', 
                    name='main' # TODO - rename this title to [M]ain menu
                )
            ),
            'quit_to_desktop': pygame.sprite.GroupSingle(
                Clickable(
                    button_x, 
                    button_offset * 7, 
                    button_width, 
                    button_height, 
                    string='E[X]it game', 
                    name='quit'
                )
            )
        }
        self.menu_items = MenuItems(items)
 
    def toggle_visiblity(self):
        self.is_visible = not self.is_visible

    def close_menu(self):
        self.is_visible = False

    def render(self, game_surface):
        """Renders all the buttons on our escape menu"""
        self.surface.fill((30, 90, 129, 225))

        self.menu_items.items['continue'].draw(self.surface)
        self.menu_items.items['continue'].sprite.render()
        self.menu_items.items['restart'].draw(self.surface)
        self.menu_items.items['restart'].sprite.render()
        self.menu_items.items['quit_to_main'].draw(self.surface)
        self.menu_items.items['quit_to_main'].sprite.render()
        self.menu_items.items['quit_to_desktop'].draw(self.surface)
        self.menu_items.items['quit_to_desktop'].sprite.render()

        game_surface.blit(self.surface, (self.width // 4,0))
