import pygame
import src.entity as entity
import src.environment
import src.colours as colours

class LightSource(entity.Entity):
    def __init__(self, x, y, width, height, image=None):
        entity.Entity.__init__(self, x, y, width, height, image)
        self.minimap_colour = colours.WHITE
        self.light = pygame.image.load('./data/light-medium.png')
        self.rect = self.light.get_rect()
