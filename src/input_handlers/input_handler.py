"""
Contains our input handler class.
This particular input handler is used for all actions
that aren't player related. i.e. navigating menus
etc...
"""
import src.game_object.tile
import src.environment
import pygame


class InputHandler():
    """Handles all inputs for the game itself
    anything related to menu navigation etc...
    is kept in here. All player input is handler
    via the PlayerInputHandler class"""

    def __init__(self, player, level):
        """
        @self.player = The player on the level
        @self.level  = The Base level.
                       This is needed to access functions that aren't
                       available in the TiledMap LevelData object
        """
        self.player = player
        self.level = level

        self.keys = {
            pygame.K_r: self.level.reset,
        }

    def process_input(self, event):
        """Processes therelated actions that are present in self.keys.
        self.keys is a mapping of keyboard input to a function.
        Note also that if we're not pressing the spacebar then we want
        to update everything in the game. The reason being is that we
        don't want to update things when we plant a bomb (press spacebar)"""
        if event.key == pygame.K_ESCAPE:
            self.level.switch_to_scene(src.environment.level_obj_list['escape-menu'])
        for key in self.keys.keys():
            if event.key == key:
                self.keys[key]()
            elif event.key != pygame.K_SPACE:
                for sprite in self.level.tiled_level.sprites:
                    if isinstance(sprite, src.game_object.tile.Triggerable):
                        sprite.update()


