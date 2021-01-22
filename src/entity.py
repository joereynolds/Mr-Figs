"""Base class for simple everyday sprite use"""

import pygame

class Entity(pygame.sprite.Sprite):
    """@Image = A pygame surface, probably a subsurface of a spritesheet. """
    def __init__(self, x, y, width, height, image=None, alpha=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.load_image(image, width, height, alpha=alpha) 
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
        self.solid = False

    def load_image(self, image, width, height, colour=None, alpha=False):
        """attempts to load an image, falls back onto a pygame surface otherwise"""
        if image:
            # Scale images up on the off-chance we've supplied a tile
            # bigger than the rest.
            return pygame.transform.scale(image, (int(width), int(height)))
        else:
            if alpha:
                return pygame.Surface((width, height)).convert_alpha()
            return pygame.Surface((width, height)).convert()
