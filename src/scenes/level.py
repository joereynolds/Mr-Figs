import copy
import src.graphics as graphics
from src.game_object.bomb import Bomb
from src.scenes.startmenu import StartMenu
from src.tiled_map import TiledMap
from src.game_object.video_tape import VideoTape
from src.level_memento import LevelMemento
import src.logger as logger
import src.scenes.scenebase as scene_base
import src.renderers.level_renderer as renderers
import src.input_handlers.global_input_handler as input_handler
from src.collision_handlers.polling_collision_handler import PollingCollisionHandler
from src.collision_handlers.turn_based_collision_handler import TurnBasedCollisionHandler
from src.user_data import UserData


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
        self.mementos = []

        scene_base.SceneBase.__init__(
            self,
            input_handler.GlobalInputHandler(
                self.player,
                self
            )
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

    def switch_to_scene(self, next_scene, start_menu=False):
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
        else: 
            self.next = Level(next_scene)
            self.game_saver.save(self.file, self.player.turns_taken, collected_tape)

    def save(self):
        state = {
            'player_x': self.player.rect.x,
            'player_y': self.player.rect.y,
            'player_destination_x': self.player.destination[0],
            'player_destination_y': self.player.destination[1],
            'player_remaining_bombs': self.player.remaining_bombs,
        }

        # TODO - Refactor this
        # I think each class should be responsible for setting
        # and restoring its own state (probably)
        # Maybe we can give all game_object a `save` and `restore`
        # method which then does the correc tthing within that class.
        for sprite in self.sprites:
            sprites_id = str(id(sprite))
            state[sprites_id] = {
                'x': None,
                'y': None,
            }
            state[sprites_id]['x'] = sprite.rect.x
            state[sprites_id]['y'] = sprite.rect.y

            if isinstance(sprite, Bomb):
                state[sprites_id]['lifespan'] = sprite.lifespan

        # print('saving', state)
        memento = LevelMemento(state)
        self.mementos.append(memento)

    def undo(self):
        """Rewinds our state to a previous one"""
        if not self.mementos:
            return

        memento = self.mementos.pop()
        state = memento.restore()
        # print('restoring', state)

        self.player.rect.x = state['player_x']
        self.player.rect.y = state['player_y']
        self.player.destination[0] = state['player_destination_x']
        self.player.destination[1] = state['player_destination_y']
        self.player.remaining_bombs = state['player_remaining_bombs']
        self.player.moving = False

        for sprite in self.sprites:
            sprites_id = str(id(sprite))
            # try:
            sprite.rect.x = state[sprites_id]['x']
            sprite.rect.y = state[sprites_id]['y']

            if isinstance(sprite, Bomb):
                sprite.lifespan = state[sprites_id]['lifespan']
            # except KeyError:
            #     print('attempted to undo a now non-existent sprite. Did it get blown up or killed?')
            #     print(sprite)

    def reset(self):
        """Reinitialises our level, kind of a hacky way
        of resetting the level again."""
        self.__init__(self.file)
