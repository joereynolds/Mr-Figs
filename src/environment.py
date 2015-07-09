"""
Handles our Scene logic and input processing/updating/rendering
"""
import pygame
import os
import levelEditor
import keys
import tile
import colours
import graphics
import guiBase
import actor

class SceneBase():
    """The base class for all scenes to inherit from."""

    def __init__(self):
        self.next = self
        self.surface = graphics.SCREEN

    def process_input(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def switch_to_scene(self,next_scene):
        self.next = next_scene
        next_scene.next = next_scene

    def terminate(self):
        pygame.quit()


class LevelBase(SceneBase):

    def __init__(self,file,next_level):
        SceneBase.__init__(self)
        self.next_level = next_level
        self.file = file
        self.level = levelEditor.TiledEditor(file)
        self.player = actor.Actor(50,50,50,50, self.level, graphics.ACTOR_SPRITE)
        self.level_tiles = self.level.level_data
        self.sprites = pygame.sprite.LayeredUpdates()
        self.sprites.add(self.level_tiles, self.player)

    def process_input(self):
        #Maybe create an InputHandler class for all of this?
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.QUIT:
                self.terminate()
            for k,v in keys.keys.items():
                if pressed_keys[k]:
                    if v == 'reset':
                        self.reset()
                        
                    else:
                        self.player.update(v)
                        for bomb in self.player.bombs:
                            bomb.bomb_collisions(self.player.bombs)
                        if v != 'space': 
                            for sprite in self.sprites:
                                if isinstance(sprite,tile.Spike):
                                    sprite.change_state()
        
    def update(self):
        self.sprites.add(self.player.bombs)
        #Move this into a function
        for bomb in self.player.bombs:
            self.sprites.add(bomb.particles)
            if bomb.particle_collision(self.player):
                self.reset()

        if self.player.finished_level():
            self.switch_to_scene(self.next_level)

    def render(self):
        self.surface.fill(colours.WHITE)        
        self.sprites.draw(self.surface)
        pygame.display.flip()

    def reset(self):
        self.__init__(self.file, self.next_level)

#Automaitc level loading
levels_dir = '../levels/'
levels = os.listdir('../levels/')
level_obj_list = [LevelBase(levels_dir + level,'temp') 
                      for level in levels 
                         if level.endswith('csv')
                 ]

for i in range(len(level_obj_list)):
    if i == len(level_obj_list)-1:
        level_obj_list[i].next_level = level_obj_list[0]
    else:
        level_obj_list[i].next_level = level_obj_list[i+1]
