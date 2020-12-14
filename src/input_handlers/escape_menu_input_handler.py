"""
Contains our input handler class.
This particular input handler is used for all actions
that aren't player related. i.e. navigating menus
etc...
"""
import src.environment
import pygame


class EscapeMenuInput():
    """Handles all inputs for the game itself
    anything related to menu navigation etc...
    is kept in here. All player input is handler
    via the PlayerInputHandler class"""

    def __init__(self, escape_menu):

        self.escape_menu = escape_menu

        self.keys = {
            pygame.K_r: 'level-1',
            pygame.K_m: 'start-menu'
        }

    def process_input(self, event):
        """Handles the scenes to go to when we
        click on certain clickable components"""
        if event.key == pygame.K_c:
            print('caleled')
            self.escape_menu.is_visible = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.escape_menu.component_dict['resume'].on_click(
                self.escape_menu.switch_to_scene, src.environment.level_obj_list['level-1']
            )
            self.escape_menu.component_dict['quit-desktop'].on_click(self.escape_menu.terminate)
