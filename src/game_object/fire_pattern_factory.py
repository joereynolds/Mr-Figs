from src.game_object.constant_fire_pattern import ConstantFirePattern
from src.game_object.burst_fire_pattern import BurstFirePattern
from src.game_object.flame_fire_pattern import FlameFirePattern

class FirePatternFactory():

    def build(self, pattern, rect, speed, level, vector):
        if pattern == 'burst':
            firer = BurstFirePattern(
                rect.centerx,
                rect.centery,
                speed,
                level,
                vector
            )

        if pattern == 'constant':
            firer = ConstantFirePattern(
                rect.centerx,
                rect.centery,
                speed,
                level,
                vector
            )
        if pattern == 'flame':
            firer = FlameFirePattern(
                rect.x,
                rect.y,
                speed,
                level,
                vector
            )

        return firer
