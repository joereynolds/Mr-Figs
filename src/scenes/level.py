import src.graphics as graphics
from src.scenes.text_overlay import TextOverlay
from src.scenes.startmenu import StartMenu
from src.tiled_map import TiledMap
from src.game_object.video_tape import VideoTape
import src.logger as logger
import src.scenes.scenebase as scene_base
import src.renderers.level_renderer as renderers
import src.input_handlers.global_input_handler as input_handler
from src.collision_handlers.polling_collision_handler import PollingCollisionHandler
from src.collision_handlers.turn_based_collision_handler import TurnBasedCollisionHandler
from src.user_data import UserData

from src.scenes.minigame.hunt.hunt import Hunt


class Level(scene_base.SceneBase):
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
        self.tiled_level = TiledMap(file, screen)
        self.player = self.tiled_level.get_player(self.tiled_level.sprites)
        self.game_saver = UserData()

        scene_base.SceneBase.__init__(
            self,
            input_handler.GlobalInputHandler(
                self.player,
                self,
                graphics.get_controller()
            ),
            graphics.get_controller()
        )

        self.file = file
        self.sprites = self.tiled_level.sprites

        # If the player has collected the tape, remove it so they
        # can't collect again
        self.remove_video_tape()
        self.game_saver.register_last_played_level(file);

        self.renderer = renderers.LevelRenderer(self)
        self.collision_handler = PollingCollisionHandler(self.player, self)
        self.turn_based_collision_handler = TurnBasedCollisionHandler(self.player, self)

    def remove_video_tape(self):
        if self.game_saver.has_video_for_level(self.file):
            tape = self.tiled_level.get_video_tape(self.tiled_level.sprites)
            self.tiled_level.sprites.remove(tape)

    def check_player_hasnt_died_a_horrible_death(self, dt):
        """If the player has been destroyed, restart the level"""
        if self.player.is_dead(dt):
            self.reset()

    def update(self, delta_time):
        if not self.renderer.escape_menu.is_visible:
            self.check_player_hasnt_died_a_horrible_death(delta_time)
            self.player.update(delta_time)

            self.sprites.update(delta_time)
            self.collision_handler.update()

            self.sprites.add(self.player.bombs)

            if self.player in self.sprites:
                self.sprites.move_to_front(self.player)

            for bomb in self.player.bombs:
                self.sprites.add(bomb.particles)

    def render(self):
        """Calls the global renderer to render"""
        self.renderer.render()

    def switch_to_scene(
        self, 
        next_scene, 
        start_menu=False, 
        video_tape_obj=False,
        minigame=False,
        ):
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

        logger.LOGGER.info('Switching to scene: ' + next_scene)

        if start_menu:
            self.reset()
            self.next = StartMenu()
        elif minigame:
            # hardcoded minigame for now
            scene = Hunt(next_scene, self)
            self.next = scene
        elif video_tape_obj:
            self.next = TextOverlay(video_tape_obj.text, video_tape_obj.redirect_to)
        else: 
            self.next = Level(next_scene)
            self.game_saver.save(self.file, collected_tape)

    def reset(self):
        """Reinitialises our level, kind of a hacky way
        of resetting the level again."""
        self.__init__(self.file)
