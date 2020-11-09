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
        self.finish_tile_collision()
        self.moveable_tile_collision()
        self.bomb_pickup_collision()

        self.bomb_collisions()
        for bomb in self.player.bombs:
            self.bomb_particle_collision(bomb)

    def bomb_collisions(self):
        """This is just a wrapper that calls the function for each bomb"""
        for _bomb in self.player.bombs:
            _bomb.bomb_collisions(self.player.bombs)

    def bomb_particle_collision(self, bomb: bomb.Bomb):
        """Returns True if any of the bombs particles collide with player.
        If they do, we'll reset the level."""
        for _bomb in self.player.bombs:
            if isinstance(_bomb, type(bomb)):
                if self.player.rect.x == _bomb.rect.x and self.player.rect.y == _bomb.rect.y and _bomb.lifespan == 0:
                    pygame.sprite.Sprite.kill(self.player)
                    return True

        for particle in bomb.particles:
            if self.player.destination[0] == particle.rect.x and self.player.destination[1] == particle.rect.y:
                pygame.sprite.Sprite.kill(self.player)
                return True
            for _tile in self.level.tiled_level.sprites:
                if isinstance(_tile, tile.Stateful):
                    if pygame.sprite.collide_rect(particle, _tile):
                        _tile.update()
                        return

    #TODO think of a good way of refactoring this
    def finish_tile_collision(self):
        """Go to the next level when we collide with the finish tile"""
        for _tile in self.level.tiled_level.sprites:
            if isinstance(_tile, tile.FinishTile):
                if self.player.destination[0] == _tile.rect.x and self.player.destination[1] == _tile.rect.y:
                    self.level.switch_to_scene(self.level.next_level)

    def bomb_pickup_collision(self):
        for _tile in self.level.tiled_level.sprites:
            if isinstance(_tile, PickupBomb):
                if self.player.destination[0] == _tile.rect.x and self.player.destination[1] == _tile.rect.y:
                    self.player.remaining_bombs += 1
                    pygame.sprite.Sprite.kill(_tile)

    def moveable_tile_collision(self):
        for _tile in self.level.tiled_level.sprites:
            if isinstance(_tile, tile.MoveableTile):
                if self.player.destination[0] == _tile.rect.x and self.player.destination[1] == _tile.rect.y:
                    _tile.rect.x = _tile.rect.x + (movement_vector.vector[self.player.direction][0] * graphics.tile_width)
                    _tile.rect.y = _tile.rect.y + (movement_vector.vector[self.player.direction][1] * graphics.tile_width)
