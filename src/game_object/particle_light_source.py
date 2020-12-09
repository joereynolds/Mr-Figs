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
        # self.image = pygame.image.load('./data/light.png')
        # self.image = pygame.transform.scale(
        #     self.image, 
        #     (
        #         self.image.get_width() * graphics.ZOOM_LEVEL * 4, 
        #         self.image.get_height() * graphics.ZOOM_LEVEL * 4
        #     )
        # )

    def generate_light(self):
        pass
