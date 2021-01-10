import src.static_scenes
import pygame
from src.event_command import EventCommand

class StartMenuInput():
    """Handles all inputs for the game itself
    anything related to menu navigation etc...
    is kept in here. All player input is handler
    via the PlayerInputHandler class"""

    def __init__(self, start_menu):
        self.start_menu = start_menu

    def process_input(self, event):
        """Handles the scenes to go to when we
        click on certain clickable components"""
        self.process__input(event)

    def process__input(self, event):
        if event['key'] == EventCommand.DOWN:
            self.start_menu.menu_items.select_next_item()
        if event['key'] == EventCommand.UP:
            self.start_menu.menu_items.select_previous_item()
        if event['key'] == EventCommand.ACTION:
            item = self.start_menu.menu_items.get_selected_item()

            if item.name == 'quit':
                pygame.quit()
                return

            item.on_selected(
                self.start_menu.switch_to_scene,
                src.static_scenes.level_obj_list[item.name]
            )
