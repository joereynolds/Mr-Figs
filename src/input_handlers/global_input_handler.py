import pygame
import src.event_handler as event_handler
import src.input_handlers.input_handler as input_handler
from src.input_handlers.player_input_handler import PlayerInputHandler
from src.input_handlers.input_handler import InputHandler


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

        self.player_input_handler = PlayerInputHandler(player)

        self.level_input_handler = InputHandler(
            self.player,
            self.level
        )

        self.event_handler = event_handler.EventHandler(level, player)

    def process_input(self, event):
        """Processes input for everything. Note that
        in certain cases we are only processing input if a key has
        been pressed. No need to process something unless needed"""
        self.event_handler.handle_events(event)
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        elif event.type == pygame.KEYDOWN:
            self.player_input_handler.process_input(event)
            self.level_input_handler.process_input(event)
