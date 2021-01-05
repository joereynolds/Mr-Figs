"""
`PollingCollisionHandler` checks for collisions per frame
"""
from src.game_object.pressure_plate import PressurePlate
from src.game_object.bullet import Bullet
from src.game_object.triggerable import Triggerable
from src.game_object.platform import Platform
from src.game_object.moving_platform import MovingPlatform
from src.game_object.enemy_pathable import EnemyPathable
from src.game_object.enemy_bombable import EnemyBombable


class PollingCollisionHandler():

    def __init__(self, player, level):
        self.player = player
        self.level = level
        self.polling_instances = (
             Bullet, 
             PressurePlate, 
             Triggerable, 
             Platform, 
             EnemyPathable,
             EnemyBombable,
             MovingPlatform,
        )

    def update(self):
        self.handle_collisions()

    def handle_collisions(self):
        for tile in self.level.tiled_level.sprites:
            if isinstance(tile, self.polling_instances):
                tile.handle_collision(None, self.player, self.level)
