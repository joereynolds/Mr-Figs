import actor
import pygame
import graphics
import environment
import level_editor
import scenes.scenebase as scene_base
import renderers.level_base_renderer as renderers
import input_handlers.global_input_handler as input_handler


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
        self.tiled_level = level_editor.LevelData(file)

        self.player = actor.Actor(
            48, 48,
            graphics.trans_width,
            graphics.trans_height,
            self,
            graphics.sprites['player']['sprites'][0]
        )

        scene_base.SceneBase.__init__(
            self,
            input_handler.GlobalInputHandler(
                self.player,
                self
            )
        )

        self.file = file
        self.next_level = next_level
        self.sprites = pygame.sprite.LayeredUpdates()
        self.sprites.add(self.tiled_level.sprites, self.player)
        self.renderer = renderers.LevelBaseRenderer(self)

    def check_player_hasnt_died_a_horrible_death(self):
        """If the player has been destroyed, restart the level"""
        if self.player not in self.sprites:
            #TODO doesn't switch to the game over screen for some reason'
            # self.switch_to_scene(environment.level_obj_list['game-over-menu'])
            self.reset()

    def update(self, delta_time):
        self.check_player_hasnt_died_a_horrible_death()
        self.player.update(delta_time)
        self.sprites.add(self.player.bombs)
        self.sprites.move_to_front(self.player)
        for bomb in self.player.bombs:
            self.sprites.add(bomb.particles)

    def render(self):
        """Calls the global renderer to render"""
        self.renderer.render()

    def reset(self):
        """Reinitialises our level, kind of a hacky way
        of resetting the level again."""
        self.__init__(self.file, self.next_level)
