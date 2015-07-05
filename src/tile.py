import entity
import graphics
import pygame


"""The tile class represents any tile in the game background or foreground.
It extends the entity class to add collision mechanics and various other bits"""
class Tile(entity.Entity):

    def __init__(self, x, y, width, height, solid, destructable, image=None):
        entity.Entity.__init__(self, x, y, width, height, image)
        self.solid = solid 
        self.destructable = destructable 
    
"""Extends Tile. If an actor collides with this class whilst it's up, the player dies"""
class Spike(Tile):
    def __init__(self, x, y, width, height, solid, destructable, image):
        Tile.__init__(self, x, y, width, height, solid, destructable, image)
        self.state = 0 
    
    def change_state(self):
        """Changes our state from 0(friendly) to 1(deadly) and vice versa.
           Changing state also requires that we change the image of our spike too"""
        if self.state:
            self.state = 0
            self.image = graphics.SPIKEDOWN_SPRITE
        else: 
            self.state = 1
            self.image = graphics.SPIKEUP_SPRITE

    def update(self):
        self.change_state()

