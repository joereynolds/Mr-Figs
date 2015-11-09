import itertools
import graphics
import bomb
import event_handler
import pygame
import tile
import collision_handler

class GlobalInputHandler():
    """Handles all input events. Key presses etc...
    Helps keep code clean...ish""" 

    keys = {
        pygame.K_u:'u',
        pygame.K_r:'reset',
        pygame.K_l:'next_level',
        pygame.K_h:'previous_level',
        pygame.K_ESCAPE:'escape'
    }

    def __init__(self, player_input_handler, level_input_handler):
        """
        @self.player = The player on the level
        @self.level = The TiledMap LevelData for this level
        @self.e_handler = An EventHandler() object
        @self.c_handler = A CollisionHandler() object
        
        """
        self.player_input_handler = player_input_handler
        self.level_input_handler = level_input_handler
        self.e_handler = event_handler.EventHandler()

    def process_input(self):
        for event in pygame.event.get():
            self.e_handler.handle_events(event)
            if event.type == pygame.KEYDOWN:
                self.player_input_handler.process_input(event)
                self.level_input_handler.process_input(event)

