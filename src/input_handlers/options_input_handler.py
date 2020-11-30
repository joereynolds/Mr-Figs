import src.environment
import pygame
import src.config as config
from src.scenes.levelbase import LevelBase


class OptionsInputHandler():
    """Handles input for the level select screen"""

    def __init__(self, level_select_menu):
        """
        @level_select_menu = The LevelMenu object
        """
        self.level_select_menu = level_select_menu

        self.keys = {
            pygame.K_1: 0,
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
                                config.level_location + self.level_select_menu.levels[self.level_select_menu.level_group_index][self.keys[key]],
                            )
                        )
            if event.key == pygame.K_ESCAPE:
                self.level_select_menu.switch_to_scene(src.environment.level_obj_list['start-menu'])
            if event.key in [pygame.K_n, pygame.K_d, pygame.K_RIGHT]:
                self.level_select_menu.go_forward()
            if event.key in [pygame.K_p, pygame.K_a, pygame.K_LEFT]:
                self.level_select_menu.go_backward()

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.level_select_menu.menu_items['next'].sprites()[0].on_click(
                self.level_select_menu.go_forward,
            )


