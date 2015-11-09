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

    def __init__(self, player, level_input_handler):
        """
        
        """
        self.player_input_handler = player.input_handler
        self.level_input_handler = level_input_handler
        self.e_handler = event_handler.EventHandler(player)

    def process_input(self):
        for event in pygame.event.get():
            self.e_handler.handle_events(event)
            if event.type == pygame.KEYDOWN:
                self.player_input_handler.process_input(event)
                self.level_input_handler.process_input(event)

