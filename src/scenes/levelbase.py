import src.game_object.actor as actor
import pygame
import src.graphics as graphics
import src.level_editor as level_editor
import src.scenes.scenebase as scene_base
import src.renderers.level_base_renderer as renderers
import src.input_handlers.global_input_handler as input_handler
import src.environment


class LevelBase(scene_base.SceneBase):
    """All levels use this class as the base level.
    So far (probably because it's huge), there has
    been no need to extend this class."""

    def __init__(self, file):#, next_level):
        """
        @file = The .tmx level file
        @next_level = A reference to the next level
        @level = A TMXMap object of the level (I think)
        @level_tiles = A sprite group of all tiles on the level
        """
        screen = graphics.get_window_surface()
        self.tiled_level = level_editor.LevelData(file, screen)

        starting_position = graphics.grid(
            int(self.tiled_level.properties.get('player_starting_x', 1)),
            int(self.tiled_level.properties.get('player_starting_y', 1))
        )

        self.player = actor.Actor(
            starting_position[0],
            starting_position[1],
            graphics.tile_width,
            graphics.tile_height,
            self,
            self.tiled_level.properties.get('player_bomb_count', 0),
            graphics.sprites['player']['sprites'][0],
        )

        scene_base.SceneBase.__init__(
            self,
            input_handler.GlobalInputHandler(
                self.player,
                self
            )
        )

        self.file = file
        self.sprites = self.tiled_level.sprites
        self.sprites.add(self.player)
        self.renderer = renderers.LevelBaseRenderer(self)

    def check_player_hasnt_died_a_horrible_death(self):
        """If the player has been destroyed, restart the level"""
        if self.player.is_dead():
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

    def switch_to_scene(self, next_scene):
        """Goes to the next scene. Note that SceneBase is
        sort of similar to a linked list in implementation.
        It is a linked list of scenes"""
        self.next = LevelBase(
            src.environment.levels[self.file]['next_level'],
        )

    def reset(self):
        """Reinitialises our level, kind of a hacky way
        of resetting the level again."""
        self.__init__(self.file)
