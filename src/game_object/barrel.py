import pygame
import src.colours as colours
import src.graphics as graphics
from src.game_object.bullet import Bullet
from src.entity import Entity
from src.game_object.constant_fire_pattern import ConstantFirePattern
from src.game_object.burst_fire_pattern import BurstFirePattern
from src.game_object.flame_fire_pattern import FlameFirePattern
from src.game_object.fire_pattern_factory import FirePatternFactory
import src.movement_vector as movement_vector

class Barrel(Entity):

    def __init__(
            self, 
            x: int, 
            y: int, 
            width: int, 
            height: int, 
            direction: str, 
            bullet_speed: int, 
            level, 
            pattern="constant",
            image=None
        ):
        Entity.__init__(self, x, y, width, height, image)
        self.vector = self.get_vector_for_direction(direction)

        self.factory = FirePatternFactory()
        self.firer = self.factory.build(
            pattern,
            self.rect,
            bullet_speed,
            level,
            self.vector
        )

    def update(self, delta_time):
        self.firer.fire(delta_time)

    def get_vector_for_direction(self, direction):
        return movement_vector.vector[direction]
