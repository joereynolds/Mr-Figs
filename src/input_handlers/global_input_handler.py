import pygame
import src.event_handler as event_handler
import src.graphics as graphics
import src.input_handlers.input_handler as input_handler
import src.logger as logger
from src.input_handlers.player_input_handler import PlayerInputHandler
from src.input_handlers.input_handler import InputHandler
from src.input_handlers.xbox_360_controller import Xbox360Controller
from src.input_handlers.keyboard_controller import KeyboardController


class GlobalInputHandler():
    """Takes all other input handler, and encapsulates them
    so that we don't get any conflicts between key presses and
    we keep code clean"""

    def __init__(self, player, level):
        """
        @player = The Actor object
        @level = The level base object
        """
        self.level = level
        self.player = player

        controller = graphics.get_controller()
        self.player_input_handler = PlayerInputHandler(player, level, controller)
        self.level_input_handler = InputHandler(player, level, controller)

        self.event_handler = event_handler.EventHandler(level, player)

    def process_input(self, event):
        """Processes input for everything. Note that
        in certain cases we are only processing input if a key has
        been pressed. No need to process something unless needed"""
        self.event_handler.handle_events(event)
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.JOYDEVICEREMOVED:
            self.player_input_handler.controller = KeyboardController
            self.level_input_handler.controller = KeyboardController
        if event.type == pygame.JOYHATMOTION or event.type == pygame.JOYBUTTONDOWN:
            if not self.level.renderer.escape_menu.is_visible:
                self.player_input_handler.process_joystick_input(event)
            self.level_input_handler.process_joystick_input(event)
        elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN: 
            if not self.level.renderer.escape_menu.is_visible:
                self.player_input_handler.process_input(event)
            self.level_input_handler.process_input(event)
