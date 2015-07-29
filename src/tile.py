import entity
import graphics
import pygame


"""The tile class represents any tile in the game background or foreground.
It extends the entity class to add collision mechanics and various other bits"""
class Tile(entity.Entity):

    def __init__(self, x, y, width, height, solid, destructable, image=None):
        entity.Entity.__init__(self, x, y, width, height, image)
        self.solid = bool(solid) 
        self.destructable = destructable 

class FinishTile(Tile):
    def __init__(self, x, y, width, height,solid, destructable, image=None):
        Tile.__init__(self, x, y, width, height, solid, destructable, image)


class Stateful(Tile):
    def __init__(self, x, y, width, height, solid, destructable, state, image, images):
        Tile.__init__(self,x,y,width,height,solid,destructable,image)
        self.state = state
        self.images = images
   
    def update(self):
        self.change_state()

    def change_state(self):
        if self.state:
            self.image = self.images[0]
            self.state = 0
        elif not self.state:
            self.image = self.images[1]
            self.state = 1

