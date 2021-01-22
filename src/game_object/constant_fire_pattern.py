import pygame
from src.game_object.bullet import Bullet

class ConstantFirePattern():

    def __init__(self, spawn_x: int, spawn_y: int, bullet_speed: int, level, vector):

        self.spawn_x = spawn_x
        self.spawn_y = spawn_y
        self.level = level
        self.bullet_speed = bullet_speed
        self.vector = vector
        self.start_time = pygame.time.get_ticks()

    def fire(self, delta_time):
        """Fires a bullet at a consistent rate"""
        elapsed = pygame.time.get_ticks() - self.start_time

        if elapsed >= 1000:
            bullet = Bullet(
                self.spawn_x,
                self.spawn_y,
                2, 
                2, 
                self.bullet_speed, 
                self.vector
            )
            self.level.sprites.add(bullet)
            self.start_time = pygame.time.get_ticks()
