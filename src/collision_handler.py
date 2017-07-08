import bomb
import tile
import pygame
import environment


class PlayerCollisionHandler():

    def __init__(self, player, level):
        self.player = player
        self.level = level

    #TODO Move this to the level object
    def get_next_level(self):
        """
        Returns an index from environment.level_obj_list of our next level
        """

        next_level_index = environment.level_obj_list.index(self.level.next_level)
        return next_level_index

    def update(self):
        self.finish_tile_collision()

        self.bomb_collisions()
        for bomb in self.player.bombs:
            self.bomb_particle_collision(bomb)

    def bomb_collisions(self):
        """This is just a wrapper that calls the function for each bomb"""
        for _bomb in self.player.bombs:
            _bomb.bomb_collisions(self.player.bombs)

    def bomb_particle_collision(self, bomb):
        """Returns True if any of the bombs particles collide with player. If they do, we'll reset the level."""
        for particle in bomb.particles:
            if pygame.sprite.collide_rect(particle,self.player) and not self.player.moving:
                pygame.sprite.Sprite.kill(self.player)
                return True
            for _tile in self.level.tiled_level.sprites:
                if isinstance(_tile, tile.Stateful):
                    if pygame.sprite.collide_rect(particle, _tile):
                        _tile.update()
                        return

    def finish_tile_collision(self):

        for _tile in self.level.tiled_level.sprites:
            if isinstance(_tile, tile.FinishTile):
                if self.player.rect.x == _tile.rect.x and self.player.rect.y == _tile.rect.y:
                    print(self.level.file)
                    self.level.switch_to_scene(environment.level_obj_list[
                        self.get_next_level()
                        ])
