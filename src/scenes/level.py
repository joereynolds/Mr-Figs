import copy
import src.graphics as graphics
from src.game_object.actor import Actor
from src.game_object.solid_tile import SolidTile
from src.game_object.pickup_bomb import PickupBomb
from src.game_object.destructible_tile import Destructible
from src.game_object.moveable_tile import MoveableTile
from src.game_object.pressure_plate import PressurePlate
from src.game_object.triggerable import Triggerable
from src.game_object.scene_switching_tile import SceneSwitchingTile
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
        # TODO - Refactor this
        # I think each class should be responsible for setting
        # and restoring its own state (probably)
        # Maybe we can give all game_object a `save` and `restore`
        # method which then does the correc tthing within that class.
        state = {}

        for sprite in self.sprites:
            sprites_id = str(id(sprite))
            state[sprites_id] = {
                'x': sprite.rect.x,
                'y': sprite.rect.y,
                'image': sprite.image,
                'type': type(sprite).__name__,
            }

            if isinstance(sprite, Actor):
                state[sprites_id]['destination_x'] = self.player.destination[0]
                state[sprites_id]['destination_y'] = self.player.destination[1]
                state[sprites_id]['remaining_bombs'] = self.player.remaining_bombs

            if isinstance(sprite, SceneSwitchingTile):
                state[sprites_id]['scene'] = sprite.scene

            if isinstance(sprite, PressurePlate):
                state[sprites_id]['state'] = sprite.state
                state[sprites_id]['triggers'] = sprite.triggers

            if isinstance(sprite, Triggerable):
                state[sprites_id]['stateful'] = sprite.stateful
                state[sprites_id]['triggered_id'] = sprite.triggered_id
                state[sprites_id]['solid'] = sprite.solid

            if isinstance(sprite, Bomb):
                state[sprites_id]['lifespan'] = sprite.lifespan

        memento = LevelMemento(state)
        self.mementos.append(memento)

    def undo(self):
        """Rewinds our state to a previous one"""
        if not self.mementos:
            return

        memento = self.mementos.pop()
        state = memento.restore()

        self.sprites.empty()
        self.player.bombs.empty()

        # The gist of it is pretty simple.
        # We recreate everything (except the player) from
        # a previous state. Definitely due a refactor
        for sprite in state:
            mementod_sprite = state[sprite]
            print(state[sprite])

            if mementod_sprite['type'] == 'Bomb':
                new_sprite = Bomb(
                    mementod_sprite['x'],
                    mementod_sprite['y'],
                    16,# mementod_sprite['width'],
                    16,# mementod_sprite['height'],
                    self.tiled_level,
                    mementod_sprite['lifespan'],
                    mementod_sprite['image']
                )
                self.sprites.add(new_sprite)
                self.player.bombs.add(new_sprite)

            # TODO - These do not correctly link when reconstructed
            # if mementod_sprite['type'] == 'PressurePlate':
            #     new_sprite = PressurePlate(
            #         mementod_sprite['x'],
            #         mementod_sprite['y'],
            #         16,# mementod_sprite['width'],
            #         16,# mementod_sprite['height'],
            #         mementod_sprite['state'],
            #         mementod_sprite['image']
            #     )
            #     new_sprite.triggers = mementod_sprite['triggers']
            #     self.sprites.add(new_sprite)

            # if mementod_sprite['type'] == 'Triggerable':
            #     new_sprite = Triggerable(
            #         mementod_sprite['x'],
            #         mementod_sprite['y'],
            #         16,# mementod_sprite['width'],
            #         16,# mementod_sprite['height'],
            #         mementod_sprite['stateful'],
            #         mementod_sprite['image'],
            #         self,
            #         mementod_sprite['triggered_id']
            #     )
            #     new_sprite.solid = mementod_sprite['solid']
            #     self.sprites.add(new_sprite)

            if mementod_sprite['type'] == 'SceneSwitchingTile':
                new_sprite = SceneSwitchingTile(
                    mementod_sprite['x'],
                    mementod_sprite['y'],
                    16,# mementod_sprite['width'],
                    16,# mementod_sprite['height'],
                    mementod_sprite['scene'],
                    mementod_sprite['image']
                )
                self.sprites.add(new_sprite)

            if mementod_sprite['type'] == 'PickupBomb':
                new_sprite = PickupBomb(
                    mementod_sprite['x'],
                    mementod_sprite['y'],
                    16,# mementod_sprite['width'],
                    16,# mementod_sprite['height'],
                    mementod_sprite['image']
                )
                self.sprites.add(new_sprite)

            if mementod_sprite['type'] == 'MoveableTile':
                new_sprite = MoveableTile(
                    mementod_sprite['x'],
                    mementod_sprite['y'],
                    16,# mementod_sprite['width'],
                    16,# mementod_sprite['height'],
                    mementod_sprite['image']
                )
                self.sprites.add(new_sprite)

            if mementod_sprite['type'] == 'Destructible':
                new_sprite = Destructible(
                    mementod_sprite['x'],
                    mementod_sprite['y'],
                    16,# mementod_sprite['width'],
                    16,# mementod_sprite['height'],
                    mementod_sprite['image']
                )
                self.sprites.add(new_sprite)

            if mementod_sprite['type'] == 'SolidTile':
                new_sprite = SolidTile(
                    mementod_sprite['x'],
                    mementod_sprite['y'],
                    16,# mementod_sprite['width'],
                    16,# mementod_sprite['height'],
                    mementod_sprite['image']
                )

                self.sprites.add(new_sprite)

            # We don't create a new player, we just modify the old one.
            # The old one has loads of logic (input and event handling etc...)
            # tied to it which would be a pain to rewire on a new class
            if mementod_sprite['type'] == 'Actor':
                self.player.rect.x = mementod_sprite['x']
                self.player.rect.y = mementod_sprite['y']
                self.player.destination[0] = mementod_sprite['destination_x'] 
                self.player.destination[1] = mementod_sprite['destination_y']
                self.player.remaining_bombs = mementod_sprite['remaining_bombs']
                self.sprites.add(self.player)
            
    def reset(self):
        """Reinitialises our level, kind of a hacky way
        of resetting the level again."""
        self.__init__(self.file)
