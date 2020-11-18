import pygame

from src.game_object.tile import Tile
from src.game_object.moveable_tile import MoveableTile
from src.movement_vector import vector
import src.graphics as graphics

class PressurePlate(Tile):
    """The PressurePlate is a tile that can be either on or off.
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

    def handle_collision(self, tile, player, level):
        for _tile in level.tiled_level.sprites:
            # TODO - rather than check every instance of the things we care about,
            # we should just be able to grab anything from the object layer (and the player)
            #
            # Update: We would be able to do this but again we need to track and update
            # the tile's position in the object layer after moving. You can see
            # an example of this in the MoveableTile.handle_collision() method.
            #
            if isinstance(_tile, (MoveableTile)):
                if pygame.sprite.collide_rect(self, _tile):
                    self.turn_on()
                else:
                    self.turn_off()
        if pygame.sprite.collide_rect(player, self):
            self.turn_on()
