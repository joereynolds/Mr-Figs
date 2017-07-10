"""
Contains our input handler class.
This particular input handler is used for all actions
that aren't player related. i.e. navigating menus
etc...
"""
import tile
import environment
import pygame


class LevelSelectInput():
    """Handles all inputs for the game itself
    anything related to menu navigation etc...
    is kept in here. All player input is handler
    via the PlayerInputHandler class"""

    def __init__(self, level_select_menu):

        self.level_select_menu = level_select_menu

        self.keys = { }

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.level_select_menu.switch_to_scene(environment.level_obj_list['start-menu'])
            for i, level in enumerate(self.level_select_menu.components):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    level.on_click(
                        self.level_select_menu.switch_to_scene, 
                        self.level_select_menu.game_levels['level-' + str(i)]
                    )

