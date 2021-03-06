"""
`TurnBasedCollisionHandler` only checks for collisions per *turn* i.e. when a
player has moved. As it's turn based this makes sense to use for the majority
of things. There are times either for technical reasons or logical reasons that
it instead makes sense to use the `PollingCollisionHandler` which checks on every
iteration (like most games do)
"""

import pygame
import src.game_object.bomb as bomb
import src.game_object.solid_tile as tile


class TurnBasedCollisionHandler():

    def __init__(self, player, level):
        self.player = player
        self.level = level

    def update(self):
        """Check for collisions against the finish tile and bombs"""
        self.handle_collisions()

        for bomb in self.player.bombs:
            bomb.bomb_collisions(self.player.bombs)
            self.bomb_particle_collision(bomb)

    def bomb_particle_collision(self, bomb: bomb.Bomb):
        """Returns True if any of the bombs particles collide with player.
        If they do, we'll reset the level."""
        for particle in bomb.particles:
            particle.handle_collision(None, self.player, self.level)

    def handle_collisions(self):
        # TODO - I *think* there's a bug here.
        # pretty sure the BombParticle needs to either be added to this list (which it might be already)
        # or that we need to add it to the PollingCollisionHandler so that it kills stuff on time.
        for _tile in self.level.tiled_level.sprites:
            if hasattr(_tile, 'handle_collision'):
                _tile.handle_collision(_tile, self.player, self.level)
