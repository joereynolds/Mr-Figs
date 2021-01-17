import pygame
from src.entity import Entity
import src.graphics as graphics
from src.movement_vector import vector

class Player(Entity):

    def __init__(
            self, 
            x: int, 
            y: int, 
            width: int, 
            height: int, 
            image=None
        ):
        self.speed = 2
        self.direction = 'nothing'
        self.next_direction = 'nothing'
        self.tail = pygame.sprite.Group()
        self.last_planted_tail = None
        self.screen_width, self.screen_height = pygame.display.get_window_size()
        Entity.__init__(self, x, y, width, height, image)


    def update(self, delta_time, level):
        if self.rect.x % graphics.tile_width == 0 and self.rect.y % graphics.tile_width == 0:
            self.create_tail(level.sprites)

            collided_sprite = pygame.sprite.spritecollideany(self, self.tail)

            if collided_sprite != self.last_planted_tail and self.direction != 'nothing':
                pygame.sprite.Sprite.kill(self)

            self.direction = self.next_direction

        self.rect.x += self.speed * vector[self.direction][0]
        self.rect.y += self.speed * vector[self.direction][1]

    def create_tail(self, level_sprites):
        tail = Entity(self.rect.x, self.rect.y, graphics.tile_width, graphics.tile_height)
        tail.image.fill((155,0 ,0))
        self.tail.add(tail)
        level_sprites.add(self.tail)
        self.last_planted_tail = tail

    def set_next_direction(self, next_direction):
        self.next_direction = next_direction

