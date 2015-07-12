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

class StartMenu(SceneBase):
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('../data/audio/BeachAudio.mp3')
        pygame.mixer.music.play()
        SceneBase.__init__(self)
        self.start_button = guiBase.ClickableElement(50,50,50,50,(150,150,150))
        self.level_button = guiBase.ClickableElement(150,50,50,50,(150,150,150))
        self.exit_button = guiBase.ClickableElement(50,200,50,50,(150,150,150)) 
        self.buttons = pygame.sprite.Group()
        self.buttons.add(self.start_button, self.exit_button, self.level_button)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.start_button.on_click(self.switch_to_scene, level_obj_list[1])
                self.exit_button.on_click(self.terminate)
    def render(self):
        self.surface.fill((255,255,255))
        self.buttons.draw(self.surface)
        self.start_button.render_text('START')
        self.exit_button.render_text('EXIT')
        
        pygame.display.flip()

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

        pygame.mixer.init()
        pygame.mixer.music.load('../data/audio/BeachAudio.mp3')
        pygame.mixer.music.play()
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
                    elif v == 'next_level':
                        self.switch_to_scene(self.next_level)
                    elif v == 'previous_level':
                        self.switch_to_scene(level_obj_list[level_obj_list.index(self)-1])
                    else:
                        pass
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

level_obj_list.insert(0, StartMenu())
for i in range(len(level_obj_list)):
    if i == len(level_obj_list)-1:
        level_obj_list[i].next_level = level_obj_list[0]
    else:
        level_obj_list[i].next_level = level_obj_list[i+1]
