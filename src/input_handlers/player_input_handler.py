import pygame

class PlayerInputHandler():
    """Handles all input processing for players"""

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

    def __init__(self, player, level):
        self.player = player
        self.level = level

    def process_input(self, event):
        for key, action in PlayerInputHandler.keys.items():
            if event.key == key:
                self.player.event_update(action)
                self.level.turn_based_collision_handler.update()
                self.player.add_turn()
