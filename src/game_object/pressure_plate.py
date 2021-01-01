import pygame

from src.game_object.moveable_tile import MoveableTile
from src.game_object.bomb import Bomb
from src.movement_vector import vector
import src.graphics as graphics
import src.entity as entity
import src.colours as colours

class PressurePlate(entity.Entity):
    """The PressurePlate is a tile that can be either on or off.
       It usually links to the Triggerable class
       so that it can affect (trigger) an effect.

       @self.state    = The starting state of the class
       @self.images   = an array of pygame surfaces
       @self.triggers = The numeric id of the Triggerable
                        if there is one to be triggered"""
    def __init__(self, x, y, width, height, state, image, images = graphics.sprites['pressure_plate']['sprites'], triggers=0):
        entity.Entity.__init__(self, x, y, width, height, image)
        self.state = state
        self.images = images
        self.triggers = triggers
        self.minimap_colour = colours.BLUE_GLOW

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
        self.turn_off()
        for _tile in level.tiled_level.sprites:
            if isinstance(_tile, (MoveableTile, Bomb)) and pygame.sprite.collide_rect(self, _tile):
                self.turn_on()
        if pygame.sprite.collide_rect(player, self):
            self.turn_on()
