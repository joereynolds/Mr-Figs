import pygame
import tile
import bomb

class CollisionHandler():

    def __init__(self, player,  level):
        self.player = player
        self.level = level

    def update(self):
        self.player_collision()

    def player_collision(self):
        """Goes through the level data assessing the correct tiles in the level that aren't itself and seeing what happens if we collide with them"""
        for sprite in self.level.data:
            if sprite.solid:
                if pygame.sprite.collide_rect(self.player, sprite):
                    pass

