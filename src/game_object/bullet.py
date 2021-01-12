import pygame
from src.game_object.bomb import Bomb
from src.game_object.solid_tile import SolidTile
from src.game_object.moveable_tile import MoveableTile
from src.entity import Entity
import src.colours as colours
import src.movement_vector as movement_vector

class Bullet(Entity):
    def __init__(self, x, y, width, height, speed, velocity, image=None):
        Entity.__init__(self, x, y, width, height, image)
        self.image.fill(colours.RED)
        self.speed = speed
        self.velocity = velocity
        self.screen_width, self.screen_height = pygame.display.get_window_size()

    def update(self, delta_time):
        self.rect.x += self.speed * self.velocity[0]
        self.rect.y += self.speed * self.velocity[1]

        if self.rect.x > self.screen_width:
            pygame.sprite.Sprite.kill(self)
        if self.rect.x < 0:
            pygame.sprite.Sprite.kill(self)
        if self.rect.y < 0:
            pygame.sprite.Sprite.kill(self)
        if self.rect.y > self.screen_height:
            pygame.sprite.Sprite.kill(self)

    def handle_collision(self, tile, player, level):
        if pygame.sprite.collide_rect(self, player):
            pygame.sprite.Sprite.kill(player)

        for _tile in level.tiled_level.sprites:
            if isinstance(_tile, Bomb) and pygame.sprite.collide_rect(self, _tile):
                pygame.sprite.Sprite.kill(self)
                _tile.lifespan = 0
                _tile.explode()

            if isinstance(_tile, (SolidTile, MoveableTile)) and pygame.sprite.collide_rect(self, _tile):
                if pygame.sprite.collide_rect(self, _tile):
                    pygame.sprite.Sprite.kill(self)
    
