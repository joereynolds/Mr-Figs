"""
Handles our Scene logic and input processing/updating/rendering
"""
import input_handler
import pygame
import os
import levelEditor
import keys
import tile
import colours
import graphics
import gui_base
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
        self.start_button = gui_base.ClickableElement(50,50,50,50,(150,150,150))
        self.level_button = gui_base.ClickableElement(150,50,50,50,(150,150,150))
        self.exit_button = gui_base.ClickableElement(50,200,50,50,(150,150,150)) 
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
        #self.level = levelEditor.TiledEditor(file)
        self.level_tiles = levelEditor.get_map_data('../levels/tmx/new-level1.tmx')#self.level.level_data
        self.player = actor.Actor(48,48,graphics.trans_width,graphics.trans_height, self.level_tiles, graphics.ACTOR_SPRITE)
        self.sprites = pygame.sprite.LayeredUpdates()
        self.sprites.add(self.level_tiles, self.player)
        self.i_handler = input_handler.InputHandler()
        self.clock = pygame.time.Clock()

    def check_player_hasnt_died_a_horrible_death(self):
        if not self.player in self.sprites:
            self.reset()

    def process_input(self):
        self.i_handler.handle_input(self.player,self) 
        
    def update(self):
        self.check_player_hasnt_died_a_horrible_death()
        self.sprites.add(self.player.bombs)
        self.sprites.move_to_front(self.player)
       
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
level_obj_list = [LevelBase(levels_dir + level,'NoNextScene') 
                      for level in levels 
                         if level.endswith('csv')
                 ]

level_obj_list.insert(0, StartMenu())
for i in range(len(level_obj_list)):
    if i == len(level_obj_list)-1:
        level_obj_list[i].next_level = level_obj_list[0]
    else:
        level_obj_list[i].next_level = level_obj_list[i+1]
