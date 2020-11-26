import src.environment
import pygame


class LevelSelectInput():
    """Handles input for the level select screen"""

    def __init__(self, level_select_menu):
        """
        @level_select_menu = The LevelMenu object
        """
        self.level_select_menu = level_select_menu

        self.keys = {
            pygame.K_1: 'level-0',
            pygame.K_2: 'level-1',
            pygame.K_3: 'level-2',
            pygame.K_4: 'level-3',
            pygame.K_5: 'level-4',
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
                        src.environment.level_obj_list[self.keys[key]]
                    )
            if event.key == pygame.K_ESCAPE:
                self.level_select_menu.switch_to_scene(src.environment.level_obj_list['start-menu'])
            if event.key in [pygame.K_n, pygame.K_d, pygame.K_RIGHT]:
                self.level_select_menu.go_forward()
            if event.key in [pygame.K_p, pygame.K_a, pygame.K_LEFT]:
                self.level_select_menu.go_backward()

        # for level in self.level_select_menu.menu_items['components']:
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         pass
                # level.on_click(
                #     self.level_select_menu.switch_to_scene,
                #     level.text.text
                # )
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.level_select_menu.menu_items['previous'].sprites()[0].on_click(
                self.level_select_menu.go_backward,
            )
            self.level_select_menu.menu_items['next'].sprites()[0].on_click(
                self.level_select_menu.go_forward,
            )


