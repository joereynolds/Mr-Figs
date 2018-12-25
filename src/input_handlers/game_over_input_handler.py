"""
Contains our input handler class.
This particular input handler is used for all actions
that aren't player related. i.e. navigating menus
etc...
"""
import environment
import pygame


class GameOverInput():

    def __init__(self, game_over_menu):
        self.game_over_menu = game_over_menu

        self.keys = {
            pygame.K_t: 'level-1',
            pygame.K_m: 'start-menu'
        }

    def process_input(self, event):
        """Handles the scenes to go to when we
        click on certain clickable components"""
        if event.type == pygame.KEYDOWN:
            for key in self.keys.keys():
                if event.key == key:
                    self.game_over_menu.switch_to_scene(
                        environment.level_obj_list[self.keys[key]]
                    )
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.game_over_menu.component_dict['main-menu'].on_click(
                self.game_over_menu.switch_to_scene, environment.level_obj_list['start-menu']
            )
            self.game_over_menu.component_dict['exit-game'].on_click(self.game_over_menu.terminate)
            self.game_over_menu.component_dict['try-again'].on_click(
                self.game_over_menu.switch_to_scene, environment.level_obj_list['level-1']
            )
