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

        self.surface = pygame.Surface((self.width, self.height)).convert_alpha()
        self.rect = self.surface.get_rect()
        asset_sizer = ResolutionAssetSizer()

        button_width, button_height = asset_sizer.get_button_size((self.width, self.height))

        x = self.rect.centerx - (button_width * 4)
        y = self.rect.top

        button_width *= 6
        button_height *= 2

        offset = button_height
        bottom = self.rect.bottom

        items = {
            'continue': pygame.sprite.GroupSingle(
                Clickable(
                    x,
                    y, 
                    button_width, 
                    button_height, 
                    string='Continue', 
                    selected=True, 
                    name='continue'
                )
            ),

            'restart': pygame.sprite.GroupSingle(
                Clickable(
                    x,
                    y + offset, 
                    button_width, 
                    button_height, 
                    string='Restart', 
                    name='restart'
                )
            ),

            'quit_to_main': pygame.sprite.GroupSingle(
                Clickable(
                    x,
                    y + offset * 2, 
                    button_width, 
                    button_height, 
                    string='Main menu', 
                    name='main'
                )
            ),
            'quit_to_desktop': pygame.sprite.GroupSingle(
                Clickable(
                    x,
                    y + offset * 3, 
                    button_width, 
                    button_height, 
                    string='Exit game', 
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
        self.surface.fill((0, 0, 0, 225))

        self.menu_items.update()
        self.menu_items.items['continue'].draw(self.surface)
        self.menu_items.items['continue'].sprite.render()
        self.menu_items.items['restart'].draw(self.surface)
        self.menu_items.items['restart'].sprite.render()
        self.menu_items.items['quit_to_main'].draw(self.surface)
        self.menu_items.items['quit_to_main'].sprite.render()
        self.menu_items.items['quit_to_desktop'].draw(self.surface)
        self.menu_items.items['quit_to_desktop'].sprite.render()

        game_surface.blit(self.surface, (0, 0))
