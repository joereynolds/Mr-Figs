"""
`PollingCollisionHandler` checks for collisions per frame
"""

from src.game_object.pressure_plate import PressurePlate
from src.game_object.triggerable import Triggerable


class PollingCollisionHandler():

    def __init__(self, player, level):
        self.player = player
        self.level = level

    def update(self):
        self.handle_collisions()

    def handle_collisions(self):
        for tile in self.level.tiled_level.sprites:
            if isinstance(tile, (PressurePlate, Triggerable)):
                tile.handle_collision(None, self.player, self.level)
