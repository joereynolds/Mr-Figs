"""
Contains our input handler class.
This particular input handler is used for all actions
that aren't player related. i.e. navigating menus
etc...
"""
import tile
import environment
import pygame


class StartMenuInput():
    """Handles all inputs for the game itself
    anything related to menu navigation etc...
    is kept in here. All player input is handler
    via the PlayerInputHandler class"""

    def __init__(self, start_menu):

        self.start_menu = start_menu

        self.keys = { }

    def process_input(self):
        """Handles the scenes to go to when we
        click on certain clickable components"""
        for event in pygame.event.get():
            for key in self.keys.keys():
                if event.key == key:
                    self.start_menu.switch_to_scene, environment.level_obj_list['start-menu']
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.start_menu.component_dict['start-game'].on_click(
                    self.start_menu.switch_to_scene, environment.level_obj_list['start-menu']
                )
                self.start_menu.component_dict['exit-game'].on_click(self.start_menu.terminate)
                self.start_menu.component_dict['level-select'].on_click(
                    self.start_menu.switch_to_scene, environment.level_obj_list['level-select']
                )
