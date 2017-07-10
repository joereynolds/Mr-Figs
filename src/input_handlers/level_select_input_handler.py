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

        self.keys = {
            pygame.K_1: 'level-0',
            pygame.K_2: 'level-1',
            pygame.K_3: 'level-2',
            pygame.K_4: 'level-3',
            pygame.K_5: 'level-4',
        }

    def process_input(self, event):
        #TODO this check is littered on every input handler
        #move it up to scene base?
        if event.type == pygame.KEYDOWN:
            for key in self.keys.keys():
                if event.key == key:
                    self.level_select_menu.switch_to_scene(
                        environment.level_obj_list[self.keys[key]]
                    )
            if event.key == pygame.K_ESCAPE:
                self.level_select_menu.switch_to_scene(environment.level_obj_list['start-menu'])
        for i, level in enumerate(self.level_select_menu.components):
            if event.type == pygame.MOUSEBUTTONDOWN:
                level.on_click(
                    self.level_select_menu.switch_to_scene, 
                    self.level_select_menu.game_levels['level-' + str(i)]
                )

