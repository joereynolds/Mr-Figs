import pygame
import src.entity as entity
import src.environment
import src.colours as colours

class LightSource(pygame.sprite.DirtySprite):
    def __init__(self, x, y, width, height, image=None):
        pygame.sprite.DirtySprite.__init__(self)
        self.minimap_colour = colours.WHITE
        # self.light = pygame.image.load('./data/light-medium.png')

        self.image = pygame.Surface((16,16)).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill((255,255,255,155))
        self.blendmode = pygame.BLEND_MULT
