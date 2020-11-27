import pygame

import src.colours as colours
import src.scenes.scenebase as scene_base
import src.input_handlers.start_menu_input_handler as input_handler
from src.gui.clickable import Clickable

class StartMenu(scene_base.SceneBase):
    """Initial start menu at the start of the game"""

    def __init__(self):
        scene_base.SceneBase.__init__(
            self,
            input_handler.StartMenuInput(self)
        )
        self.components = pygame.sprite.LayeredUpdates()

        size = pygame.display.get_window_size()
        center_x = size[0] // 2

        self.menu_items = {
            'start-button': pygame.sprite.GroupSingle(Clickable(center_x, 100, 100, 50, '[S]TART GAME')),
            'level-select': pygame.sprite.GroupSingle(Clickable(center_x, 200, 100, 50, '[L]EVEL SELECT')),
            'options': pygame.sprite.GroupSingle(Clickable(center_x, 300, 100, 50, '[O]PTIONS')),
            'quit': pygame.sprite.GroupSingle(Clickable(center_x, 400, 100, 50, '[Q]UIT'))

        }

    def render(self):
        """Fill our surface and render our buttons"""
        self.surface.fill(colours.BLUE_GLOW)
        self.menu_items['start-button'].draw(self.surface)
        self.menu_items['start-button'].sprite.render_text()
        self.menu_items['level-select'].draw(self.surface)
        self.menu_items['level-select'].sprite.render_text()
        self.menu_items['options'].draw(self.surface)
        self.menu_items['options'].sprite.render_text()
        self.menu_items['quit'].draw(self.surface)
        self.menu_items['quit'].sprite.render_text()
