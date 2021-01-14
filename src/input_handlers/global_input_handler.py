import pygame
import src.event_handler as event_handler
import src.graphics as graphics
import src.input_handlers.input_handler as input_handler
import src.logger as logger
from src.input_handlers.player_input_handler import PlayerInputHandler
from src.input_handlers.input_handler import InputHandler
from src.input_handlers.xbox_360_controller import Xbox360Controller
from src.input_handlers.keyboard_controller import KeyboardController
from src.event_command import EventCommand


class GlobalInputHandler():
    """Takes all other input handler, and encapsulates them
    so that we don't get any conflicts between key presses and
    we keep code clean"""

    def __init__(self, player, level, controller):
        """
        @player = The Actor object
        @level = The level base object
        """
        self.level = level
        self.player = player

        self.player_input_handler = PlayerInputHandler(player, level)
        self.level_input_handler = InputHandler(player, level, controller)

        self.event_handler = event_handler.EventHandler(level, player)

    def process_input(self, event):
        """Processes input for everything. Note that
        in certain cases we are only processing input if a key has
        been pressed. No need to process something unless needed"""
        self.event_handler.handle_events(event['raw_event'])
        if event['raw_event'].type == pygame.QUIT:
            pygame.quit()
        if event['raw_event'].type == pygame.JOYDEVICEREMOVED:
            self.player_input_handler.controller = KeyboardController
            self.level_input_handler.controller = KeyboardController
        elif event['raw_event'].type in [pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN, pygame.JOYHATMOTION, pygame.JOYBUTTONDOWN]: 
            if event['key'] == EventCommand.ESCAPE:
                self.level.renderer.escape_menu.toggle_visiblity()

            if event['key'] == EventCommand.SECONDARY_ACTION:
                self.level.renderer.minimap.toggle_visiblity()

            # debugging only
            if event['raw_event'].type == pygame.KEYDOWN:
                if event['raw_event'].key == pygame.K_n:
                    self.level.switch_to_scene(self.level.tiled_level.properties['next_level'])
                if event['raw_event'].key == pygame.K_b:
                    self.level.tiled_level.map_layer_for_camera.zoom += 0.5
            # end debugging

            if not self.level.renderer.escape_menu.is_visible:
                self.player_input_handler.process_input(event)
            if self.level.renderer.escape_menu.is_visible:
                self.level_input_handler.process_input(event)
