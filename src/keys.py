import pygame

keys = {pygame.K_UP:'up',
        pygame.K_DOWN:'down',
        pygame.K_LEFT:'left',
        pygame.K_RIGHT:'right',
        pygame.K_SPACE:'space',
        pygame.K_u:'u',
        pygame.K_r:'reset',
        pygame.K_l:'next_level',
        pygame.K_h:'previous_level'
        }

opposites = {'up':'down',
             'down':'up',
             'left':'right',
             'right':'left'} #This is used to map 'up' to 'down', 'left' to 'right' etc... 
               #So that we can undo a users action if needed.
