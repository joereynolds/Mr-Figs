import src.static_scenes
import pygame
import src.config as config
from src.scenes.level import Level
from src.user_data import UserData
from src.event_command import EventCommand


class OptionsInputHandler():
    """Handles input for the options menu"""

    def __init__(self, menu):
        self.menu = menu
        self.save = UserData()

    def process_input(self, event):
        """
        Process either the clicks on a certain level
        or the presses of a key and redirect to that
        level.
        """
        if event['key'] == EventCommand.DOWN:
            self.menu.menu_items.select_next_item()
        if event['key'] == EventCommand.UP:
            self.menu.menu_items.select_previous_item()
        if event['key'] == EventCommand.ACTION:
            item = self.menu.menu_items.get_selected_item()

            if item.name == 'clear_data':
                self.save.delete_save_data()
            
            if item.name == 'toggle_music':
                self.save.toggle_music_option()

            if item.name == 'go_back':
                self.menu.switch_to_scene(src.static_scenes.level_obj_list['start-menu'])

        # TODO -get this working again
#         if event.type == pygame.MOUSEBUTTONDOWN:

#             self.level_select_menu.menu_items['toggle_music'].sprite.on_click(
#                 self.level_select_menu.menu_items['toggle_music'].sprite.toggle,
#                 self.save.toggle_music_option
#             )

#             self.level_select_menu.menu_items['clear_data'].sprite.on_click(
#                 self.save.delete_save_data
#             )

#             self.level_select_menu.menu_items['go_back'].sprite.on_click(
#                 self.level_select_menu.switch_to_scene,
#                 src.static_scenes.level_obj_list['start-menu']
#             )

