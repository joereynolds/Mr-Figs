import src.environment
import pygame
import src.config as config
from src.scenes.level import Level
from src.user_data import UserData


class OptionsInputHandler():
    """Handles input for the level select screen"""

    def __init__(self, level_select_menu):
        """
        @level_select_menu = The LevelMenu object
        """
        self.level_select_menu = level_select_menu
        self.save = UserData()

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
            if event.key == pygame.K_ESCAPE:
                self.level_select_menu.switch_to_scene(src.environment.level_obj_list['start-menu'])

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.level_select_menu.menu_items['toggle_music'].sprite.on_click(
                self.level_select_menu.menu_items['toggle_music'].sprite.toggle,
                self.save.toggle_music_option
            )
            self.level_select_menu.menu_items['clear_data'].sprite.on_click(
                self.save.delete_save_data
            )
