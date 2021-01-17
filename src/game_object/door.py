import pygame

from src.game_object.solid_tile import SolidTile
import src.graphics as graphics
from src.entity import Entity
import src.colours

class Door(Entity):
    """Like the Triggerable class but way simpler."""
    def __init__(self, x, y, width, height, image):
        Entity.__init__(self, x, y, width, height, image)
        self.images = [
            graphics.subsurf(graphics.grid(0,9)),
            graphics.subsurf(graphics.grid(1,9)),
        ]
        self.open = False

    def open_door(self):
        self.image = self.images[1]
        self.open = True

    def handle_collision(self, tile, player, level):
        if player.destination[0] == self.rect.x and player.destination[1] == self.rect.y and not self.open:
            player.destination[0] = player.rect.x
            player.destination[1] = player.rect.y

    def handle_pre_bomb_particle_creation(self, level):
        """Changes how we handle bomb creation on whether our door is open or not"""
        return self.open
