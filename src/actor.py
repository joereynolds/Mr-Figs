import pygame
import keys
import bomb
import entity
import colours
import tile
import input_handler
import graphics


class Actor(entity.Entity):

    def __init__(self, x, y, width, height, level, image=None):
        entity.Entity.__init__(self, x, y, width, height, image)

        self.direction = 'down'
        self.speed = graphics.trans_width
        self.level = level
        self.bombs = pygame.sprite.Group()
        self.move_stack = [] #contains the last 10 moves the user did. We keep this so that a user can undo their actions. 
        self.i_handler = input_handler.InputHandler()

    def move(self,command):
        self.i_handler.handle_player_input(self,command) 

    def collide(self):
        """Goes through the level data assessing the correct tiles in the level that aren't itself and seeing what happens if we collide with them"""
        for sprite in self.level.level_data:
            if sprite.solid :
                if pygame.sprite.collide_rect(self,sprite):
                    self.update(keys.opposites[self.move_stack.pop()]) #'undo' our action.
            if isinstance(sprite, tile.Stateful):
                if not sprite.state:
                    if pygame.sprite.collide_rect(self, sprite):
                        pygame.sprite.Sprite.kill(self)

    def finished_level(self):
        """Returns True if the user has finished level. i.e. if they have
           destroyed the block and gotten out of the boundaries of the screen"""
        for sprite in self.level.level_data:
            if isinstance(sprite, tile.FinishTile):
                if pygame.sprite.collide_rect(self, sprite):
                    return True
    
    def undo_action(self):
        if self.move_stack:
            self.move(keys.opposites[self.move_stack.pop()]) #undo

    def update(self, command):
        if command == 'space':
            self.create_bomb()
        elif command == 'u':
            self.undo_action()
        else:
            self.move(command)
            self.move_stack.append(command)
            self.collide()
            self.update_bombs()
            self.finished_level()

    def create_bomb(self):
        self.bombs.add(bomb.Bomb(self.rect.x,
                                 self.rect.y,
                                 graphics.trans_width,
                                 graphics.trans_height,
                                 self.level,
                                 graphics.BOMB_SPRITE_5))
           
    def update_bombs(self):
 
        for bomb in self.bombs:
            bomb.image = bomb.images[-bomb.lifespan]
            bomb.lifespan -= 1
            if bomb.blow_up():
                self.bombs.remove(bomb)

