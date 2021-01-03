import pygame
import src.colours as colours
from src.game_object.bullet import Bullet
from src.entity import Entity
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
        self.direction = direction
        self.vector = self.get_vector_for_direction(self.direction)
        self.level = level
        self.bullet_timer = 1
        self.bullet_speed = bullet_speed
        self.shots = 0
        self.time_elapsed = 0

        self.pattern = pattern
        self.pattern_map = {
            "constant": self.constant_fire,
            "burst": self.burst_fire
        }

    def update(self, delta_time):
        self.pattern_map[self.pattern](delta_time)

    def constant_fire(self, delta_time):
        """Fires a bullet at a consistent rate"""
        self.bullet_timer-= delta_time
        if self.bullet_timer <= 0:
            bullet = Bullet(
                self.rect.centerx, 
                self.rect.centery, 
                2, 
                2, 
                self.bullet_speed, 
                self.direction
            )
            self.level.sprites.add(bullet)
            self.bullet_timer = 1

    def burst_fire(self, delta_time):
        """Fires a group of 3 bullets in a burst"""
        self.bullet_timer-= delta_time
        self.time_elapsed += delta_time

        if self.bullet_timer <= 0:
            if self.time_elapsed >= 0.125:
                bullet = Bullet(
                    self.rect.centerx, 
                    self.rect.centery, 
                    2, 
                    2, 
                    self.bullet_speed, 
                    self.direction
                )
                self.level.sprites.add(bullet)
                self.shots += 1
                self.time_elapsed = 0

        if self.shots >= 3:
            self.bullet_timer = 1
            self.shots = 0

    def get_vector_for_direction(self, direction):
        return movement_vector.vector[direction]
