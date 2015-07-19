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

class FinishTile(Tile):
    def __init__(self, x, y, width, height,solid, destructable, image=None):
        Tile.__init__(self, x, y, width, height, solid, destructable, image)

    
"""Extends Tile. If an actor collides with this class whilst it's up, the player dies"""
class Spike(Tile):
    def __init__(self, x, y, width, height, solid, destructable, state, image):
        Tile.__init__(self, x, y, width, height, solid, destructable, image)
        self.state = state 
        self.images = [graphics.SPIKEMID_SPRITE, graphics.SPIKEUP_SPRITE]
    
    def change_state(self):
        """Changes our state from 0(friendly) to 1(deadly) and vice versa.
           Changing state also requires that we change the image of our spike too"""
        if self.state:
            self.image = graphics.SPIKEDOWN_SPRITE
            self.state = 0
        else: 
            self.image = graphics.SPIKEUP_SPRITE
            self.state = 1
            self.animate()

    def animate(self):
        for image in self.images:
             self.image = image

    def update(self):
        self.change_state()

