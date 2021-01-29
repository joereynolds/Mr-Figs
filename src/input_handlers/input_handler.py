"""
Contains our input handler class.
This particular input handler is used for all actions
that aren't player related. i.e. navigating menus
etc...
"""
import src.game_object.solid_tile
from src.scenes.startmenu import StartMenu
from src.event_command import EventCommand
import src.static_scenes
import pygame


class InputHandler():
    """Handles all inputs for the game itself
    anything related to menu navigation etc...
    is kept in here. All player input is handler
    via the PlayerInputHandler class"""

    def __init__(self, player, level, controller):
        """
        @self.player = The player on the level
        @self.level  = The Base level.
                       This is needed to access functions that aren't
                       available in the TiledMap object
        """
        self.player = player
        self.level = level
        self.controller = controller

    def process_input(self, event):
        """Processes the related actions that are present in self.keys.
        self.keys is a mapping of keyboard input to a function.
        Note also that if we're not pressing the spacebar then we want
        to update everything in the game. The reason being is that we
        don't want to update things when we plant a bomb (press spacebar)"""
        if event['key'] == EventCommand.UP:
            self.level.renderer.escape_menu.menu_items.select_previous_item()
        if event['key'] == EventCommand.DOWN:
            self.level.renderer.escape_menu.menu_items.select_next_item()
        if event['key'] == EventCommand.ACTION:

            item = self.level.renderer.escape_menu.menu_items.get_selected_item()

            if item.name == 'continue':
                self.level.renderer.escape_menu.close_menu()
            if item.name == 'restart':
                self.level.reset()
            if item.name == 'main':
                self.level.switch_to_scene('start-menu', True)
            if item.name == 'quit':
                pygame.quit()
