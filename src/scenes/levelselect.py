import pygame

import os
import src.colours as colours
import src.scenes.scenebase as scene_base
import src.input_handlers.level_select_input_handler as input_handler
from src.gui.clickable import Clickable
from src.gui.level_select_item import LevelSelectItem

class LevelMenu(scene_base.SceneBase):

    def __init__(self, levels):
        """
        @levels A dict of our levels that comes from environment.create_level_list
        """
        self.size = pygame.display.get_window_size()
        self.width = self.size[0]
        self.height = self.size[1]
        self.level_group_index = 0
        self.image = pygame.image.load('./data/background-scene.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.menu_items = {
            'components': pygame.sprite.LayeredUpdates(),
            'previous': pygame.sprite.GroupSingle(),
            'next':  pygame.sprite.GroupSingle()
        }

        self.levels = self.get_levels()
        self.add_levels_to_sprite_group(self.levels[self.level_group_index])


        self.menu_items['previous'].add(
            Clickable(25, self.height // 2, 50, 50, 'FIRST 10')
        )

        self.menu_items['next'].add(
            Clickable(self.width - 75, self.height // 2, 50, 50, 'NEXT 10')
        )

        scene_base.SceneBase.__init__(
            self,
            input_handler.LevelSelectInput(
                self
            )
        )

    def go_forward(self):
        if self.level_group_index < 2:
            self.level_group_index += 1
            self.add_levels_to_sprite_group(self.levels[self.level_group_index])

    def go_backward(self):
        if (self.level_group_index > 0):
            self.level_group_index -= 1
            self.add_levels_to_sprite_group(self.levels[self.level_group_index])

    def get_levels(self):
        levels = [
            [
                "tutorial-bombing.tmx",
                "tutorial-movement.tmx",
                "tutorial-picking-up-easy.tmx",
                "tutorial-picking-up-easy.tmx",
                "tutorial-picking-up-easy.tmx",
                "tutorial-picking-up-easy.tmx",
                "tutorial-picking-up-easy.tmx",
                "tutorial-picking-up-easy.tmx",
                "tutorial-picking-up-easy.tmx",
                "tutorial-picking-up-easy.tmx",
            ],
            [
                "tutorial-portals.tmx",
                "tutorial-pressure-plate.tmx",
                "tutorial-pushing.tmx",
                "tutorial-pressure-plate.tmx",
                "tutorial-pressure-plate.tmx",
                "tutorial-pressure-plate.tmx",
                "tutorial-pressure-plate.tmx",
                "tutorial-pressure-plate.tmx",
                "tutorial-pressure-plate.tmx",
                "tutorial-pressure-plate.tmx",
            ],
            [
                "lotta-lasers.tmx",
                "sneaky-bastard.tmx",
                "tutorial-picking-up.tmx",
                "sneaky-bastard.tmx",
                "sneaky-bastard.tmx",
                "sneaky-bastard.tmx",
                "sneaky-bastard.tmx",
                "sneaky-bastard.tmx",
                "sneaky-bastard.tmx",
                "sneaky-bastard.tmx",
            ]
        ]

        return levels

    def add_levels_to_sprite_group(self, levels):
        self.menu_items['components'].empty()
        x = self.width // 14
        y = self.height // 2

        button_width = self.width // 6
        button_height = self.height // 4
        spacing = 25

        # render first five of the group
        for j in range(5):
            self.menu_items['components'].add([
                LevelSelectItem(
                    x + (j * (button_width + spacing)),
                    button_height * 1,
                    button_width,
                    button_height,
                    levels[j],
                    j + 1
                ),
            ])

        # render second five of the group
        for j in range(5, 10):
            self.menu_items['components'].add([
                LevelSelectItem(
                    x + ((j - 5) * (button_width + spacing)),
                    button_height * 2 + spacing,
                    button_width,
                    button_height,
                    levels[j],
                    j + 1 if j < 9 else 0
                ),
            ])

    def render(self):
        """Renders a button for each level that is in the game"""
        self.surface.blit(self.image, ((0,0)))
        self.menu_items['components'].draw(self.surface)

        for component in self.menu_items['components']:
            component.render_text()

        if self.level_group_index > 0:
            self.menu_items['previous'].draw(self.surface)

        if self.level_group_index < 2:
            self.menu_items['next'].draw(self.surface)
