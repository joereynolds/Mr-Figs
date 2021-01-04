import pygame
import src.colours as colours
import src.graphics as graphics
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
        self.vector = self.get_vector_for_direction(direction)
        self.level = level
        self.bullet_timer = 1
        self.bullet_speed = bullet_speed
        self.shots = 0
        self.time_elapsed = 0

        self.flames = pygame.sprite.LayeredUpdates()
        self.flame_cooldown = 2
        self.pattern = pattern
        self.pattern="flame"
        self.pattern_map = {
            "flame": self.flame_fire,
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
                self.vector
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
                    self.vector
                )
                self.level.sprites.add(bullet)
                self.shots += 1
                self.time_elapsed = 0

        if self.shots >= 3:
            self.bullet_timer = 1
            self.shots = 0

    def flame_fire(self, delta_time):
        """Creates a burst of fire spanning 3 tiles"""
        self.bullet_timer-= delta_time
        self.time_elapsed += delta_time


        print(self.time_elapsed)
        # if self.flame_cooldown < 0:
        if not len(self.flames):
            if self.bullet_timer <= 0:
                fire_one = Bullet(
                    self.rect.x + (graphics.tile_width * self.vector[0]), 
                    self.rect.y + (graphics.tile_width * self.vector[1]), 
                    graphics.tile_width, 
                    graphics.tile_width, 
                    self.bullet_speed, 
                    (0,0)
                )

                fire_two = Bullet(
                    self.rect.x + ((graphics.tile_width * 2) * self.vector[0]), 
                    self.rect.y + (graphics.tile_width * self.vector[1]), 
                    graphics.tile_width, 
                    graphics.tile_width, 
                    self.bullet_speed, 
                    (0,0)
                )
                # fire_three = Bullet(
                #     self.rect.centerx + (graphics.tile_width * self.vector[0]), 
                #     self.rect.centery + (graphics.tile_width * self.vector[1]), 
                #     graphics.tile_width, 
                #     graphics.tile_width, 
                #     self.bullet_speed, 
                #     (0,0)
                # )

                self.flames.add(fire_one)
                self.flames.add(fire_two)
                self.level.sprites.add(self.flames)
                self.flame_cooldown = 2

        if len(self.flames):
            self.flame_cooldown -= delta_time

        if self.time_elapsed >= 2 and len(self.flames):
            self.level.sprites.remove(self.flames)
            self.flames.empty()
            self.time_elapsed = 0

    def get_vector_for_direction(self, direction):
        return movement_vector.vector[direction]
