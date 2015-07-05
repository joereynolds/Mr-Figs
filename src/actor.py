import pygame
import keys
import bomb
import entity
import colours
import tile
import graphics


class Actor(entity.Entity):

    def __init__(self, x, y, width, height, level, image=None):
        entity.Entity.__init__(self, x, y, width, height, image)

        self.image.fill(colours.RED)
        self.direction = 'down'
        self.lives = 3 
        self.speed = 50
        self.level = level
        self.bombs = pygame.sprite.Group()
        self.move_stack = [] #contains the last 10 moves the user did. We keep this so that a user can undo their actions. 

    def move(self,command):
        directions = {'up':(0,-1),
                      'down':(0,1),
                      'left':(-1,0),
                      'right':(1,0),
                      'nothing':(0,0)}

        self.rect.x += directions[command][0] * self.speed
        self.rect.y += directions[command][1] * self.speed
        self.direction = command 

    def collide(self):
        for sprite in self.level.created_level:
            if sprite.solid:
                if pygame.sprite.collide_rect(self,sprite):
                    self.update(keys.opposites[self.move_stack.pop()]) #'undo' our action.
            if isinstance(sprite, tile.Spike):
                if not sprite.state:
                    if pygame.sprite.collide_rect(self, sprite):
                        pygame.sprite.Sprite.kill(self)

    def finished_level(self):
        """Returns True if the user has finished level. i.e. if they have
           destroyed the block and gotten out of the boundaries of the screen"""
        if self.rect.x >= graphics.WIDTH or \
           self.rect.x <= 0 or \
           self.rect.y > graphics.HEIGHT or \
           self.rect.y <= 0:
           return True
    
    def undo_action(self):
        if self.move_stack:
            self.move(keys.opposites[self.move_stack.pop()]) #undo

    def update(self, command):
        if command == 'space':
            self.bombs.add(bomb.Bomb(self.rect.x,
                                   self.rect.y,
                                   50,
                                   50,
                                   self.level))
        elif command == 'u':
            self.undo_action()
        else:
            self.move(command)
            self.move_stack.append(command)
            self.collide()
            self.update_bombs()
            self.finished_level()
           
    def update_bombs(self):
        for bomb in self.bombs:
            bomb.lifespan -= 1
            if bomb.blow_up():
                self.bombs.remove(bomb)

