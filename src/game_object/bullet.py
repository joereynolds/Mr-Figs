import pygame
from src.game_object.solid_tile import SolidTile
from src.game_object.moveable_tile import MoveableTile
from src.entity import Entity
import src.colours as colours
import src.movement_vector as movement_vector

class Bullet(Entity):
    def __init__(self, x, y, width, height, direction, image=None):
        Entity.__init__(self, x, y, width, height, image)
        self.minimap_colour = colours.RED
        self.image.fill(colours.RED)
        self.speed = 2
        self.velocity = movement_vector.vector[direction]

    def update(self, delta_time):
        self.rect.x += self.speed * self.velocity[0]
        self.rect.y += self.speed * self.velocity[1]

    def handle_collision(self, tile, player, level):
        if pygame.sprite.collide_rect(self, player):
            pygame.sprite.Sprite.kill(player)

        for _tile in level.tiled_level.sprites:
            if isinstance(_tile, (SolidTile)) and pygame.sprite.collide_rect(self, _tile):
                if pygame.sprite.collide_rect(self, _tile):
                    pygame.sprite.Sprite.kill(self)
    
