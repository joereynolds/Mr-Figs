import pygame

keys = {pygame.K_UP:'up',
        pygame.K_DOWN:'down',
        pygame.K_LEFT:'left',
        pygame.K_RIGHT:'right',
        pygame.K_SPACE:'space',
        pygame.K_u:'u',
        1:'nothing'}#be does nothing but we need to supply a command to our update function for the player. And sometimes we want  no movement to take effect  

opposites = {'up':'down',
             'down':'up',
             'left':'right',
             'right':'left'} #This is used to map 'up' to 'down', 'left' to 'right' etc... 
               #So that we can undo a users action if needed.
