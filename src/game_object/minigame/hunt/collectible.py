import pygame
from src.entity import Entity

class Collectible(Entity):

    def __init__(
            self, 
            x: int, 
            y: int, 
            width: int, 
            height: int, 
            image=None
        ):
        Entity.__init__(self, x, y, width, height, image)
