"""
`TurnBasedCollisionHandler` only checks for collisions per *turn* i.e. when a
player has moved. As it's turn based this makes sense to use for the majority
of things. There are times either for technical reasons or logical reasons that
it instead makes sense to use the `PollingCollisionHandler` which checks on every
iteration (like most games do)
"""

import pygame
import src.game_object.bomb as bomb
import src.game_object.tile as tile
import src.graphics as graphics
from src.game_object.pressure_plate import PressurePlate
from src.game_object.triggerable import Triggerable


class PollingCollisionHandler():

    def __init__(self, player, level):
        self.player = player
        self.level = level

    def update(self):
        """Check for collisions against the finish tile and bombs"""
        self.handle_collisions()

    def handle_collisions(self):
        for tile in self.level.tiled_level.sprites:
            if isinstance(tile, (PressurePlate, Triggerable)):
                tile.handle_collision(None, self.player, self.level)
