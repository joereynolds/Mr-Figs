import actor
import pygame
import colours
import graphics
import levelEditor
import input_handler
import collision_handler 
import scenes.scenebase as scene_base
import scenes.escapemenu as escape_menu

class LevelBase(scene_base.SceneBase):

    def __init__(self,file,next_level):
        scene_base.SceneBase.__init__(self)
        self.file = file
        self.next_level = next_level
        self.level = levelEditor.LevelData(file)
        self.level_tiles = self.level.data
        self.player = actor.Actor(48, 48,
                                  graphics.trans_width,
                                  graphics.trans_height,
                                  self.level,
                                  graphics.sprites['player']['sprites'][0])
        self.sprites = pygame.sprite.LayeredUpdates()
        self.sprites.add(self.level_tiles, self.player)
        self.i_handler = input_handler.InputHandler(self.player, self.level, self)
        self.c_handler = self.i_handler.c_handler
        self.clock = pygame.time.Clock()
        self.escape_menu = escape_menu.EscapeMenu()
        self.menu_open = False

    def render_escape_menu(self):
        """Adds the escape menu to ours sprites group therefore
        getting rendered to the screen"""
        if not self.menu_open:
            self.sprites.add(self.escape_menu.components)
            self.menu_open = True
        else : 
            self.sprites.remove(self.escape_menu.components)
            self.menu_open = False

    def check_player_hasnt_died_a_horrible_death(self):
        """If the player has been destroyed, restart the level"""
        if not self.player in self.sprites:
            self.reset()

    def process_input(self):
        self.i_handler.handle_input() 
        
    def update(self):
        delta = self.clock.tick(60) / 1000.0
        self.player.update(delta)
        self.c_handler.update()
        self.check_player_hasnt_died_a_horrible_death()
        self.sprites.add(self.player.bombs)
        self.sprites.move_to_front(self.player)
       
        #Move this into a function
        for bomb in self.player.bombs:
            self.sprites.add(bomb.particles)
            if self.c_handler.bomb_particle_collision(bomb):
                self.reset()
        
    def render(self):
        self.surface.fill(colours.WHITE)        
        self.sprites.draw(self.surface)
        pygame.display.flip()

    def reset(self):
        self.__init__(self.file, self.next_level)


