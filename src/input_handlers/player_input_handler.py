import pygame
from src.event_command import EventCommand

class PlayerInputHandler():
    """Handles all input processing for players.
    This is meant to be extendable so that in theory,
    we can pass this class to 400 players and they could
    all handle their input with minimal extra effort from me."""

    def __init__(self, player, level):
        self.player = player
        self.level = level

    def process_input(self, event):
        """
        Event here is a dict returned from EventCommand
        """
        if event['key'] != 'nothing':
            self.player.event_update(event['key'])
            self.level.turn_based_collision_handler.update()
