import pygame
import tile
import bomb


class CollisionHandler():

    def __init__(self, player, level):
        self.player = player
        self.level = level

    def update(self):
        self.player_collision()
        self.bomb_collisions()       
        for bomb in self.player.bombs:
            self.bomb_particle_collision(bomb)
 
    def player_collision(self):
        """Goes through the level data assessing the correct tiles in the level that aren't itself and seeing what happens if we collide with them"""
        for sprite in self.level.data:
            if sprite.solid:
                if pygame.sprite.collide_rect(self.player, sprite):
                    pass
            if isinstance(sprite, tile.FinishTile):
                if pygame.sprite.collide_rect(self.player, sprite):
                    return 'SIGNAL HERE TO LET LEVEL KNOW THE PLAYER HAS FINISHED THE LEVEL'

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
            for _tile in self.level.data:
                if isinstance(_tile, tile.Stateful):
                    if pygame.sprite.collide_rect(particle, _tile):
                        _tile.update()
                        return


