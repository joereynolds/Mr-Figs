import pygame
class KeyboardController():
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

        # xbox controller

        #button
        0: 'nothing',
        1: 'space',

        #hats (dpad)
        (1, 0): 'right',
        (-1, 0): 'left',
        (0, 1): 'up',
        (0, -1): 'down',
        (0, 0): 'nothing',

        # Weird in between values, just try and guess them
        # best we can
        (1, 1): 'up',
        (-1, 1): 'up',
        (1, -1): 'down',
        (-1, -1): 'down',
    }
