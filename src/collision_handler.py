import pygame
import src.bomb as bomb
import src.tile as tile
import src.graphics as graphics
import src.movement_vector as movement_vector
from src.pickup_bomb import PickupBomb


class PlayerCollisionHandler(object):

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
        if isinstance(bomb, type(bomb)):
            if self.player.rect.x == bomb.rect.x and self.player.rect.y == bomb.rect.y:
                if bomb.lifespan == 0:
                    pygame.sprite.Sprite.kill(self.player)
                    return True
            if self.player.destination[0] == bomb.rect.x and self.player.destination[1] == bomb.rect.y:
                # Bit of a hack but if 5 is our max lifespan for a bomb then it's impossible to be
                # travelling to it and for it to have that lifespan since we would have moved
                # and decreased the bomb's lifespan
                if bomb.lifespan != 0 and bomb.lifespan < 5:
                    pygame.sprite.Sprite.kill(bomb)
                    self.player.add_bomb()

        for particle in bomb.particles:
            if self.player.destination[0] == particle.rect.x and self.player.destination[1] == particle.rect.y:
                pygame.sprite.Sprite.kill(self.player)
                return True
            for _tile in self.level.tiled_level.sprites:
                if isinstance(_tile, tile.Stateful):
                    if pygame.sprite.collide_rect(particle, _tile):
                        _tile.update()
                        return

    def handle_collisions(self):
        for _tile in self.level.tiled_level.sprites:
            if hasattr(_tile, 'handle_collision'):
                _tile.handle_collision(self.player, self.level)
