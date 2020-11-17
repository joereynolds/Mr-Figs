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
        self.get_levels()

        # Left arrow
        self.components.add(Clickable(25, 400, 50, 50 ,'FIRST 10'))

        # Right arrow
        self.components.add(Clickable(700, 400, 50, 50, 'NEXT 10' ))

    def get_levels(self):
        size = pygame.display.get_window_size()
        width = size[0]
        height = size[1]
        x = width // 4
        y = height // 2
        levels = os.listdir('./data/levels/tmx')
        level_button_width = 100
        level_button_height = 25

        self.components.empty()

        for i in range(1, 2):
            for j in range(5):
                self.components.add([
                    Clickable(x + (j * 125) , 75 * i, level_button_width, level_button_height, levels[j]),
                    ])

        for i in range(2, 3):
            for j in range(5, 10):
                self.components.add([
                    Clickable(x + ((j - 5) * 125) , 75 * i, level_button_width, level_button_height, levels[j]),
                    ])

    def render(self):
        """Renders a button for each level that is in the game"""
        self.surface.fill(colours.BLUE_GLOW)
        self.components.draw(self.surface)
        for component in self.components:
            component.render_text()
