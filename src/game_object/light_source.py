import pygame
import src.entity as entity
import src.environment
import src.colours as colours
import src.graphics as graphics
from src.entity import Entity

class LightSource(Entity):
    def __init__(self, x, y, width, height):
        entity.Entity.__init__(self, x, y, width, height, None)
        self.minimap_colour = colours.WHITE

        self.image = pygame.image.load('./data/light.png')
        self.image = pygame.transform.scale(
            self.image, 
            (
                self.image.get_width() * graphics.ZOOM_LEVEL * 4, 
                self.image.get_height() * graphics.ZOOM_LEVEL * 4
            )
        )
