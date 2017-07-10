"""
Contains our input handler class.
This particular input handler is used for all actions
that aren't player related. i.e. navigating menus
etc...
"""
import tile
import environment
import pygame


class InputHandler():
    """Handles all inputs for the game itself
    anything related to menu navigation etc...
    is kept in here. All player input is handler
    via the PlayerInputHandler class"""

    def __init__(self, player, level, level_base):
        """
        @self.player     = The player on the level
        @self.level      = The TiledMap LevelData for this level
        @self.level_base = The Base level.
                           This is needed to access functions that aren't
                           available in the TiledMap LevelData object
        """
        self.player = player
        self.level = level
        self.level_base = level_base

        self.keys = {
            # pygame.K_ESCAPE: self.level_base.escape_menu.toggle,
            pygame.K_r: self.level_base.reset,
        }

    def process_input(self, event):
        """Processes therelated actions that are present in self.keys.
        self.keys is a mapping of keyboard input to a function.
        Note also that if we're not pressing the spacebar then we want
        to update everything in the game. The reason being is that we
        don't want to update things when we plant a bomb (press spacebar)"""
        if event.key == pygame.K_ESCAPE:
            self.level_base.switch_to_scene(environment.level_obj_list[2])
        for key in self.keys.keys():
            if event.key == key:
                self.keys[key]()
            elif event.key != pygame.K_SPACE:
                for sprite in self.level.sprites:
                    if isinstance(sprite, tile.Triggerable):
                        sprite.update()


