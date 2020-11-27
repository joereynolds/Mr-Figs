import src.environment
import pygame
from src.scenes.levelbase import LevelBase


class LevelSelectInput():
    """Handles input for the level select screen"""

    def __init__(self, level_select_menu):
        """
        @level_select_menu = The LevelMenu object
        """
        self.level_select_menu = level_select_menu
        self.level_dir = './data/levels/tmx/'

        """
        When we press a number, it should take
        us to that entry in the level list.
        For example, pressing '1' should take
        us to the first entry in the list.
        We also respect the next and previous buttons
        so that if we press next and then 1 it would be that entry + 10
        0 means 10 in our case.
        """
        self.keys = {
            pygame.K_1: 0,
            pygame.K_2: 1,
            pygame.K_3: 2,
            pygame.K_4: 3,
            pygame.K_5: 4,
            pygame.K_6: 5,
            pygame.K_7: 6,
            pygame.K_8: 7,
            pygame.K_9: 8,
            pygame.K_0: 9,
        }

    def process_input(self, event):
        """
        Process either the clicks on a certain level
        or the presses of a key and redirect to that
        level.
        """
        if event.type == pygame.KEYDOWN:
            for key in self.keys.keys():
                if event.key == key:
                    self.level_select_menu.switch_to_scene(
                            LevelBase(
                                self.level_dir + self.level_select_menu.levels[self.level_select_menu.level_group_index][self.keys[key]],
                            )
                        )
            if event.key == pygame.K_ESCAPE:
                self.level_select_menu.switch_to_scene(src.environment.level_obj_list['start-menu'])
            if event.key in [pygame.K_n, pygame.K_d, pygame.K_RIGHT]:
                self.level_select_menu.go_forward()
            if event.key in [pygame.K_p, pygame.K_a, pygame.K_LEFT]:
                self.level_select_menu.go_backward()

        for level in self.level_select_menu.menu_items['components']:
            if event.type == pygame.MOUSEBUTTONDOWN:
                level.on_click(
                    self.level_select_menu.switch_to_scene,
                    LevelBase(self.level_dir + level.text.text)
                )
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.level_select_menu.menu_items['previous'].sprites()[0].on_click(
                self.level_select_menu.go_backward,
            )
            self.level_select_menu.menu_items['next'].sprites()[0].on_click(
                self.level_select_menu.go_forward,
            )


