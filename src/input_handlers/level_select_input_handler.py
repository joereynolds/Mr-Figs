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
        #TODO this check is littered on every input handler
        #move it up to scene base?
        if event.type == pygame.KEYDOWN:
            for key in self.keys.keys():
                if event.key == key:
                    self.level_select_menu.switch_to_scene(
                        src.environment.level_obj_list[self.keys[key]]
                    )
            if event.key == pygame.K_ESCAPE:
                self.level_select_menu.switch_to_scene(src.environment.level_obj_list['start-menu'])
        for i, level in enumerate(self.level_select_menu.components):
            if event.type == pygame.MOUSEBUTTONDOWN:
                level.on_click(
                    self.level_select_menu.switch_to_scene,
                    self.level_select_menu.game_levels['level-' + str(i)]
                )

