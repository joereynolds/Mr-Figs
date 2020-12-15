"""
Instead of an image, uses particles (we'll see)
"""
import pygame
import src.entity as entity
import src.environment
import src.colours as colours
import src.graphics as graphics

class LightSource(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.minimap_colour = colours.WHITE

        self.particles = pygame.sprite.Group()

    def generate_light(self):
        pass
