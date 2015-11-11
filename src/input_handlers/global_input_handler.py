import pygame
import event_handler
import collision_handler

class GlobalInputHandler():
    """Takes all other input handler, and encapsulates them
    so that we don't get any conflicts between key presses and
    we keep code clean"""

    keys = {
        pygame.K_u:'u',
        pygame.K_r:'reset',
        pygame.K_l:'next_level',
        pygame.K_h:'previous_level',
        pygame.K_ESCAPE:'escape'
    }

    def __init__(self, player, level):
        """
        
        """
        self.level = level
        self.player = player
        self.player_input_handler = player.input_handler
        self.level_input_handler = level.i_handler
        self.e_handler = event_handler.EventHandler(player)

    def process_input(self):
        """Processes input for everything. Note that
        in certain cases we are only processing input if a key has
        been pressed. No need to process something unless needed"""
        for event in pygame.event.get():
            self.e_handler.handle_events(event)
            self.level.escape_menu.process_input(event)
            if event.type == pygame.KEYDOWN:
                self.player_input_handler.process_input(event)
                self.level_input_handler.process_input(event)

