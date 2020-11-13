import pygame
import src.game_object.bomb as bomb
import src.game_object.tile as tile
import src.graphics as graphics
import src.movement_vector as movement_vector
from src.game_object.pickup_bomb import PickupBomb


class PlayerCollisionHandler(object):

    def __init__(self, player, level):
        self.player = player
        self.level = level

    def update(self):
        """Check for collisions against the finish tile and bombs"""
        self.handle_collisions()

        for bomb in self.player.bombs:
            bomb.bomb_collisions(self.player.bombs)
            # bomb.handle_collision(self.player)
            self.bomb_particle_collision(bomb)

    def bomb_particle_collision(self, bomb: bomb.Bomb):
        """Returns True if any of the bombs particles collide with player.
        If they do, we'll reset the level."""
        for particle in bomb.particles:
            particle.handle_collision(self.player, self.level)

    def handle_collisions(self):
        for _tile in self.level.tiled_level.sprites:
            if hasattr(_tile, 'handle_collision'):
                _tile.handle_collision(self.player, self.level)
