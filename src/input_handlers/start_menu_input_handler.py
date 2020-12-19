"""
Contains our input handler class.
This particular input handler is used for all actions
that aren't player related. i.e. navigating menus
etc...
"""
import src.environment
import pygame


class StartMenuInput():
    """Handles all inputs for the game itself
    anything related to menu navigation etc...
    is kept in here. All player input is handler
    via the PlayerInputHandler class"""

    def __init__(self, start_menu):
        """
        self.keys is a list of keybindings for each scene
            pygame.K_s: 'level-1',
        Simply means that when we press 's' we will be taken to level-1
        """

        self.start_menu = start_menu

        self.keys = {
            pygame.K_s: 'level-select',
            pygame.K_o: 'options-menu'
        }

    def process_input(self, event):
        """Handles the scenes to go to when we
        click on certain clickable components"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()

            for key in self.keys.keys():
                if event.key == key:
                    self.start_menu.switch_to_scene(
                        src.environment.level_obj_list[self.keys[key]]
                    )

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.start_menu.menu_items['start-button'].sprite.on_click(
                self.start_menu.switch_to_scene, 
                src.environment.level_obj_list['level-select']
            )

            self.start_menu.menu_items['quit'].sprite.on_click(self.start_menu.terminate)
