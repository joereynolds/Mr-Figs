import pygame

import src.colours as colours
import src.scenes.scenebase as scene_base
from src.input_handlers.options_input_handler import OptionsInputHandler
from src.gui.clickable import Clickable
from src.gui.checkbox import Checkbox

class OptionsMenu(scene_base.SceneBase):
    """Options menu for toggling music etc..."""

    def __init__(self):
        scene_base.SceneBase.__init__(
            self,
            OptionsInputHandler(self)
        )
        self.components = pygame.sprite.LayeredUpdates()

        size = pygame.display.get_window_size()
        self.image = pygame.image.load('./data/background-scene.png')
        self.image = pygame.transform.scale(self.image, (size[0], size[1]))
        center_x = size[0] // 2

        self.menu_items = {
            'toggle_music': pygame.sprite.GroupSingle(Checkbox(center_x, 0, 50, 50, 0)),
            'clear_data': pygame.sprite.GroupSingle(Clickable(center_x, 100, 100, 50, 'CLEAR GAME DATA')),
            'go_back': pygame.sprite.GroupSingle(Clickable(center_x, 200, 100, 50, '[B]ACK'))
        }

    def render(self):
        """Fill our surface and render our buttons"""
        self.surface.blit(self.image, ((0,0)))

        self.menu_items['toggle_music'].draw(self.surface)
        self.menu_items['clear_data'].draw(self.surface)
        self.menu_items['go_back'].draw(self.surface)
        self.menu_items['toggle_music'].sprite.render()
        self.menu_items['clear_data'].sprite.render()
        self.menu_items['go_back'].sprite.render()
