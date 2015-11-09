"""

"""

import itertools
import graphics
import bomb
import event_handler
import pygame
import tile
import collision_handler



class InputHandler():
    """Handlws all inputs for the game itself
    anything related to menu navigation etc...
    is kept in here. All player input is handler
    via the PlayerInputHandler class"""

    keys = {
        pygame.K_r:'reset',
        pygame.K_l:'next_level',
        pygame.K_h:'previous_level',
        pygame.K_ESCAPE:'escape'
    }

    def __init__(self, player, level, level_base):
        """
        @self.player = The player on the level
        @self.level = The TiledMap LevelData for this level
        @self.e_handler = An EventHandler() object
        @self.c_handler = A CollisionHandler() object
        @self.level_base = The Base level. This is needed to access functions that aren't available in the TiledMap LevelData object 
        
        """
        self.player = player
        self.level = level
        self.level_base = level_base
        self.e_handler = event_handler.EventHandler()
        self.i = 0 #REMOVE THIS

    def process_input(self, event):
         for k,v in InputHandler.keys.items():
            if event.key == k:
                if v == 'escape' :
                    self.level_base.escape_menu.toggle()
                if v == 'reset':
                    self.level_base.reset()
                elif v == 'next_level':
                    self.level_base.switch_to_scene(self.level_base.next_level)
                else: 
                    if v != 'space':#don't change state on the spikes when we plant a bomb
                        for sprite in self.level.data:
                            if isinstance(sprite, tile.Triggerable):
                                sprite.update()
    def process_input_old(self):
        for event in pygame.event.get():
            if event.type == 28:
                for _bomb in self.player.bombs:
                    _bomb.animate()
            if event.type == 29:
                for _bomb in self.player.bombs:
                    for particle in _bomb.particles:
                        particle.image = graphics.sprites['explosion']['sprites'][self.i]
                self.i +=1
                if self.i >5 :
                    self.i = 0
                #This is handled terribly. We should be using delta times for ANY animation. 
