import actor
import pygame
import colours
import graphics
import level_editor
import collision_handler 
import scenes.scenebase as scene_base
import scenes.escapemenu as escape_menu
import renderers.global_renderer as grenderers
import renderers.level_base_renderer as renderers
import input_handlers.input_handler as input_handler
import input_handlers.global_input_handler as g_i_handler


class LevelBase(scene_base.SceneBase):
    """All levels use this class as the base level.
    So far (probably because it's huge), there has
    been no need to extend this class."""

    def __init__(self, file, next_level):
        """
        @file = The .tmx level file
        @next_level = A reference to the next level
        @level = A TMXMap object of the level (I think)
        @level_tiles = A sprite group of all tiles on the level
        """
        scene_base.SceneBase.__init__(self)
        self.file = file
        self.next_level = next_level
        self.level = level_editor.LevelData(file)
        self.player = actor.Actor(
            48, 48,
            graphics.trans_width,
            graphics.trans_height,
            self.level,
            graphics.sprites['player']['sprites'][0]
        )
        self.sprites = pygame.sprite.LayeredUpdates()
        self.sprites.add(self.level.sprites, self.player)
        self.escape_menu = escape_menu.EscapeMenu()

        self.gi_handler = g_i_handler.GlobalInputHandler(
            self.player,
            self.level,
            self
        )

        #rendering
        self.renderer = renderers.LevelBaseRenderer(self)
        self.g_renderer = grenderers.GlobalRenderer(self)

        #seems like an easy (albeit feels hacky) way to move all sprites at once?
        #useful for centering our level on the screen
        #for sprite in self.sprites:
        #    sprite.rect.x += 96



    def check_player_hasnt_died_a_horrible_death(self):
        """If the player has been destroyed, restart the level"""
        if not self.player in self.sprites:
            self.reset()

    def process_input(self):
        """Process the input for the level via the global
        input handler"""
        self.gi_handler.process_input()

    def update(self, delta_time):
        self.check_player_hasnt_died_a_horrible_death()
        self.player.update(delta_time)
        self.sprites.add(self.player.bombs)
        self.sprites.move_to_front(self.player)
        for bomb in self.player.bombs:
            self.sprites.add(bomb.particles)

    def render(self):
        """Calls the global renderer to render"""
        self.g_renderer.render()

    def reset(self):
        """Reinitialises our level, kind of a hacky way
        of resetting the level again."""
        self.__init__(self.file, self.next_level)
