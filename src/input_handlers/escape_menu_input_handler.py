"""
Contains our input handler class.
This particular input handler is used for all actions
that aren't player related. i.e. navigating menus
etc...
"""
import tile
import environment
import pygame


class EscapeMenuInput():
    """Handles all inputs for the game itself
    anything related to menu navigation etc...
    is kept in here. All player input is handler
    via the PlayerInputHandler class"""

    def __init__(self, escape_menu):

        self.escape_menu = escape_menu

        self.keys = { }

    def process_input(self):
        """Handles the scenes to go to when we
        click on certain clickable components"""
        for event in pygame.event.get():
            for key in self.keys.keys():
                if event.key == key:
                    self.level_select_menu.switch_to_scene, environment.level_obj_list['start-menu']
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.level_select_menu.component_dict['start-game'].on_click(
                    self.level_select_menu.switch_to_scene, environment.level_obj_list['start-menu']
                )
                self.level_select_menu.component_dict['exit-game'].on_click(self.level_select_menu.terminate)
                self.level_select_menu.component_dict['level-select'].on_click(
                    self.level_select_menu.switch_to_scene, environment.level_obj_list['level-select']
                )
