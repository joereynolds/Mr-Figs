from src.game_object.tile import Tile
import src.graphics as graphics

class Switch(Tile):
    """The switch class is a tile that can be either on or off.
       It usually links to the Triggerable class
       so that it can affect (trigger) an effect.

       @self.state    = The starting state of the class
       @self.images   = an array of pygame surfaces
       @self.triggers = The numeric id of the Triggerable
                        if there is one to be triggered"""
    def __init__(self, x, y, width, height, solid, destructable, state, image, images = graphics.sprites['switch']['sprites'], triggers=0):
        Tile.__init__(self, x, y, width, height, solid, destructable, image)
        self.state = state
        self.images = images
        self.triggers = triggers

    def update(self):
        self.change_state()

    def change_state(self):
        if self.state:
            self.turn_off()
        elif not self.state:
            self.turn_on()

    def turn_on(self):
        self.image = self.images[1]
        self.state = 1

    def turn_off(self):
        self.image = self.images[0]
        self.state = 0

