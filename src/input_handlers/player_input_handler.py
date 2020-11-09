import pygame

class PlayerInputHandler():
    """Handles all input processing for players.
    This is meant to be extendable so that in theory,
    we can pass this class to 400 players and they could
    all handle their input with minimal extra effort from me."""

    keys = {
        pygame.K_UP:'up',
        pygame.K_DOWN:'down',
        pygame.K_LEFT:'left',
        pygame.K_RIGHT:'right',

        pygame.K_SPACE:'space',

        pygame.K_w: 'up',
        pygame.K_a: 'left',
        pygame.K_s: 'down',
        pygame.K_d: 'right',

        pygame.K_h: 'left',
        pygame.K_j: 'down',
        pygame.K_k: 'up',
        pygame.K_l: 'right',
    }

    def __init__(self, player):
        self.player = player

    def process_input(self, event):
        for key, action in PlayerInputHandler.keys.items():
            if event.key == key:
                self.player.event_update(action)
                self.player.collision_handler.update()
