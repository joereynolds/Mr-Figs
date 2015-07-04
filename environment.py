"""
Handles our Scene logic and input processing/updating/rendering
"""
import pygame
import levelEditor
import keys
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
        self.level = levelEditor.Editor(file)
        self.player = actor.Actor(50,50,50,50, self.level)
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)
        self.level_tiles = self.level.created_level

    def process_input(self):
        pressed_keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.QUIT:
                self.terminate()
            for k,v in keys.keys.items():
                if pressed_keys[k]:
                    self.player_group.update(v)

    def update(self):
        self.player_group.add(self.player.bombs)

        #Move this into a function
        for bomb in self.player.bombs:
            self.player_group.add(bomb.particles)
        if self.player.finished_level():
            self.switch_to_scene(self.next_level)

    def render(self):
        self.surface.fill(colours.WHITE)        
        self.level.created_level.draw(self.surface)
        self.player_group.draw(self.surface)
        pygame.display.flip()

Level3 = LevelBase('level3.txt','Nothing')
Level2 = LevelBase('level2.txt', Level3)
Level1 = LevelBase('level1.txt',Level2) 
