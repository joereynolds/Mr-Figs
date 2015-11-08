import pygame
import gui_base
import environment

class LevelSelectContainer(pygame.sprite.Sprite):
    """Container for the components for the level select menu.
    Note that self.components is iterating through the level_list
    so can find out how many levels there are"""

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.components = [
            gui_base.Clickable(x*i, y*i ,width,height) 
                for i, level in enumerate(environment.create_level_list())
        ]

    def update(self):
        pass

    def render(self):
        pass


