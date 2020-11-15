import pygame

import os
import src.colours as colours
import src.scenes.scenebase as scene_base
import src.input_handlers.level_select_input_handler as input_handler
from src.gui.clickable import Clickable

class LevelMenu(scene_base.SceneBase):

    def __init__(self, levels):
        """
        @levels A dict of our levels that comes from environment.create_level_list
        """
        scene_base.SceneBase.__init__(
            self,
            input_handler.LevelSelectInput(
                self
            )
        )

        self.components = pygame.sprite.LayeredUpdates()

        size = pygame.display.get_window_size()
        center_x = size[0] // 2

        for i, level in enumerate(os.listdir('./data/levels/tmx')):
            self.components.add([Clickable(center_x, 75 * i, 100, 25, level), ])


    def render(self):
        """Renders a button for each level that is in the game"""
        self.surface.fill(colours.BLUE_GLOW)
        self.components.draw(self.surface)
        for component in self.components:
            component.render_text()
