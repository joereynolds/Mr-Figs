import pygame

import src.graphics as graphics
from src.game_object.bullet import Bullet

class FlameFirePattern():

    def __init__(self, spawn_x: int, spawn_y: int, bullet_speed: int, level, vector):
        self.bullet_timer = 1
        self.time_elapsed = 0
        self.flame_cooldown = 0
        self.spawn_x = spawn_x
        self.spawn_y = spawn_y
        self.level = level
        self.bullet_speed = bullet_speed
        self.vector = vector
        self.flames = pygame.sprite.LayeredUpdates()
        

    def fire(self, delta_time):
        """Creates a burst of fire spanning 3 tiles"""
        self.bullet_timer-= delta_time
        self.time_elapsed += delta_time
        self.flame_cooldown -= delta_time

        if not len(self.flames) and self.flame_cooldown <= 0:
            if self.bullet_timer <= 0:
                fire_one = Bullet(
                    self.spawn_x,
                    self.spawn_y,
                    graphics.tile_width, 
                    graphics.tile_width, 
                    self.bullet_speed, 
                    (0,0)
                )
                fire_two = Bullet(
                    self.spawn_x + ((graphics.tile_width * 1) * self.vector[0]), 
                    self.spawn_y + ((graphics.tile_width * 1) * self.vector[1]), 
                    graphics.tile_width, 
                    graphics.tile_width, 
                    self.bullet_speed, 
                    (0,0)
                )
                fire_three = Bullet(
                    self.spawn_x + ((graphics.tile_width * 2) * self.vector[0]), 
                    self.spawn_y + ((graphics.tile_width * 2) * self.vector[1]), 
                    graphics.tile_width, 
                    graphics.tile_width, 
                    self.bullet_speed, 
                    (0,0)
                )

                self.flames.add(fire_one)
                self.flames.add(fire_two)
                self.flames.add(fire_three)
                self.level.sprites.add(self.flames)
                self.flame_cooldown = 2

        if self.time_elapsed >= 2 and len(self.flames):
            self.level.sprites.remove(self.flames)
            self.flames.empty()
            self.time_elapsed = 0

