import itertools
import graphics
import bomb
import event_handler
import pygame
import tile
import collision_handler


class InputHandler():
    """Handles all input events. Key presses etc...
    Helps keep code clean...ish""" 

    keys = {pygame.K_UP:'up',
            pygame.K_DOWN:'down',
            pygame.K_LEFT:'left',
            pygame.K_RIGHT:'right',
            pygame.K_SPACE:'space',
            pygame.K_u:'u',
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
        self.c_handler = collision_handler.CollisionHandler(self.player, level)
        self.i = 0 #REMOVE THIS

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == 27:
                for laser in self.level.data:
                    pass
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

            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                for k,v in InputHandler.keys.items():
                    if event.key == k:
                        if v == 'escape' :
                            self.level_base.escape_menu.toggle()
                        if v == 'reset':
                            self.level_base.reset()
                        elif v == 'next_level':
                            self.level_base.switch_to_scene(self.level_base.next_level)
                        else: 
                            self.player.event_update(v)
                            self.c_handler.update()
                            if v != 'space':#don't change state on the spikes when we plant a bomb
                                for sprite in self.level.data:
                                    if isinstance(sprite, tile.Triggerable):
                                        sprite.update()
