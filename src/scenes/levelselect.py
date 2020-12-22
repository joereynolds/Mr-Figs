import src.graphics as graphics
from src.scenes.level import Level
from src.game_object.scene_switching_tile import SceneSwitchingTile
from src.renderers.level_select_renderer import LevelSelectRenderer
from src.tiled_map import TiledMap
from src.game_object.video_tape import VideoTape
import src.logger as logger
import src.scenes.scenebase as scene_base
import src.renderers.level_renderer as renderers
import src.input_handlers.global_input_handler as input_handler
from src.collision_handlers.polling_collision_handler import PollingCollisionHandler
from src.collision_handlers.turn_based_collision_handler import TurnBasedCollisionHandler
from src.user_data import UserData


class LevelSelect(scene_base.SceneBase):
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
        logger.LOGGER.info('Creating level select: ' + file)

        screen = graphics.get_window_surface()
        self.tiled_level = TiledMap(file, screen)
        self.player = self.tiled_level.get_player(self.tiled_level.sprites)
        self.game_saver = UserData()

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

        self.scene_switching_tiles = []

        for sprite in self.sprites:
            if isinstance(sprite, SceneSwitchingTile):
                self.scene_switching_tiles.append(sprite)
                # If the stair's scene is the same as our last played level,
                # then put our sprite near those stairs
                if sprite.scene == self.game_saver.get_last_played_level():
                    self.player.rect.x = sprite.rect.x
                    self.player.rect.y = sprite.rect.y - graphics.tile_height
                    self.player.destination[0] = sprite.rect.x
                    self.player.destination[1] = sprite.rect.y - graphics.tile_height

        self.renderer = LevelSelectRenderer(self)
        self.collision_handler = PollingCollisionHandler(self.player, self)
        self.turn_based_collision_handler = TurnBasedCollisionHandler(self.player, self)

    def update(self, delta_time):
        self.player.update(delta_time)

    def render(self):
        """Calls the global renderer to render"""
        self.renderer.render()

    def switch_to_scene(self, next_scene):
        """Goes to the next scene. Note that SceneBase is
        sort of similar to a linked list in implementation.
        It is a linked list of scenes"""
        logger.LOGGER.info('Switching to scene: ' + next_scene)
        self.next = Level(next_scene)

    def reset(self):
        """Reinitialises our level, kind of a hacky way
        of resetting the level again."""
        self.__init__(self.file)
