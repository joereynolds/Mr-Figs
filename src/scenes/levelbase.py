import src.graphics as graphics
import src.level_editor as level_editor
from src.game_object.video_tape import VideoTape
import src.logger as logger
import src.scenes.scenebase as scene_base
import src.renderers.level_base_renderer as renderers
import src.input_handlers.global_input_handler as input_handler
from src.collision_handlers.polling_collision_handler import PollingCollisionHandler
from src.collision_handlers.turn_based_collision_handler import TurnBasedCollisionHandler
from src.save import SaveGame


class LevelBase(scene_base.SceneBase):
    """All levels use this class as the base level.
    So far (probably because it's huge), there has
    been no need to extend this class."""

    def __init__(self, file):
        """
        @file = The .tmx level file
        @next_level = A reference to the next level
        @level = A TMXMap object of the level (I think)
        @level_tiles = A sprite group of all tiles on the level
        """
        logger.LOGGER.info('Creating level: ' + file)

        screen = graphics.get_window_surface()
        self.tiled_level = level_editor.LevelData(file, screen)
        self.player = self.tiled_level.get_player(self.tiled_level.sprites)
        self.game_saver = SaveGame()

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

        # If the player has collected the tape, remove it so they
        # can't collect again
        self.remove_video_tape()

        self.renderer = renderers.LevelBaseRenderer(self)
        self.collision_handler = PollingCollisionHandler(self.player, self)
        self.turn_based_collision_handler = TurnBasedCollisionHandler(self.player, self)

    def remove_video_tape(self):
        if self.game_saver.has_video_for_level(self.file):
            tape = self.tiled_level.get_video_tape(self.tiled_level.sprites)
            self.tiled_level.sprites.remove(tape)

    def check_player_hasnt_died_a_horrible_death(self):
        """If the player has been destroyed, restart the level"""
        if self.player.is_dead():
            self.reset()

    def update(self, delta_time):
        self.check_player_hasnt_died_a_horrible_death()
        self.player.update(delta_time)

        self.sprites.update()
        self.collision_handler.update()

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
        # TODO - Pretty ugly
        collected_tape = None
        if self.tiled_level.properties.get('has_video_tape', False):
            collected_tape = True
            for sprite in self.sprites:
                if isinstance(sprite, VideoTape):
                    collected_tape = False

        self.game_saver.save(self.file, self.player.turns_taken, collected_tape)

        logger.LOGGER.info('Switching to scene: ' + next_scene)
        self.next = LevelBase(next_scene)

    def reset(self):
        """Reinitialises our level, kind of a hacky way
        of resetting the level again."""
        self.__init__(self.file)
