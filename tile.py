import entity
import pygame


"""The tile class represents any tile in the game background or foreground.
It extends the entity class to add collision mechanics and various other bits"""
class Tile(entity.Entity):

    def __init__(self, x, y, width, height, solid, destructable, image=None):
        entity.Entity.__init__(self, x, y, width, height, image)
        self.solid = solid 
        self.destructable = destructable 
    
    
