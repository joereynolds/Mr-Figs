"""Base class for simple everyday sprite use"""

import pygame

class Entity(pygame.sprite.Sprite):
    """@Image = A pygame surface, probably a subsurface of a spritesheet. """
    def __init__(self, x, y, width, height, image=None):
        pygame.sprite.Sprite.__init__(self)

        self.image = image if image else pygame.Surface((width, height)).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
