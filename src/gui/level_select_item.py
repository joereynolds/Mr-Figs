"""
This is the card that displays on the level select menu for
each level.
"""
import pygame
from src.gui.clickable import Clickable

class LevelSelectItem(Clickable):

    def __init__(self, x, y, width, height, string, image = './data/placeholder-card-image.png'):
        Clickable.__init__(self, x, y, width, height, string)

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))

        self.shaded_area = pygame.Surface(
            (self.image.get_width(), self.image.get_height()), 
            flags=pygame.SRCALPHA
        )

        self.shaded_area.fill((50, 50, 50, 0))
        self.image.blit(self.shaded_area, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)

        # self.rect = self.image.get_rect() 
        # self.rect.x = x
        # self.rect.y = y



