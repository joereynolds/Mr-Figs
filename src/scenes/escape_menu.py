import pygame
import src.colours as colours
import src.config as config
import src.scenes.scenebase as scene_base
import src.input_handlers.escape_menu_input_handler as input_handler
from src.gui.clickable import Clickable

class EscapeMenu(scene_base.SceneBase):
    """The menu that pops up during game when we press escape"""

    def __init__(self):
        scene_base.SceneBase.__init__(self, input_handler.EscapeMenuInput(self)) 

        self.is_visible = False
        self.width, self.height = pygame.display.get_window_size()

        self.surface = pygame.Surface((self.width // 2, self.height - 64)).convert_alpha()

        self.menu_items = {
            'continue': pygame.sprite.GroupSingle(),
            'restart': pygame.sprite.GroupSingle(),
            'quit_to_main':  pygame.sprite.GroupSingle(),
            'quit_to_desktop':  pygame.sprite.GroupSingle()
        }

        button_x = self.surface.get_width() // 4
        button_width = self.surface.get_width() // 2

        self.menu_items['continue'].add(
            Clickable(
                button_x, 
                100, 
                button_width,
                50, '[C]ontinue'
            )
        )

        self.menu_items['restart'].add(
            Clickable(
                button_x, 
                200, 
                button_width,
                50, 
                '[R]estart'
            )
        )

        self.menu_items['quit_to_main'].add(
            Clickable(
                button_x, 
                300, 
                button_width,
                50, 
                '[Q]uit to title screen'
            )
        )

        self.menu_items['quit_to_desktop'].add(
            Clickable(
                button_x, 
                400, 
                button_width, 
                50, 
                'E[X]it game'
            )
        )

    def toggle_visiblity(self):
        self.is_visible = not self.is_visible

    def close_menu(self):
        self.is_visible = False

    def render(self, game_surface):
        """Renders all the buttons on our escape menu"""
        self.surface.fill((30, 90, 129, 225))

        self.menu_items['continue'].draw(self.surface)
        self.menu_items['continue'].sprite.render()

        self.menu_items['restart'].draw(self.surface)
        self.menu_items['restart'].sprite.render()

        self.menu_items['quit_to_main'].draw(self.surface)
        self.menu_items['quit_to_main'].sprite.render()

        self.menu_items['quit_to_desktop'].draw(self.surface)
        self.menu_items['quit_to_desktop'].sprite.render()

        game_surface.blit(self.surface, (self.width // 4,0))
