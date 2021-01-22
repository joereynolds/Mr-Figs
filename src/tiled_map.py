from src.game_object.switch_tile import Switch
from src.game_object.scene_switching_tile import SceneSwitchingTile
from src.game_object.pressure_plate import PressurePlate
from src.game_object.triggerable import Triggerable
from src.game_object.portal import Portal
from src.game_object.destructible_tile import Destructible
from src.game_object.torch import Torch
from src.game_object.solid_tile import SolidTile
from src.game_object.path import Path
from src.game_object.platform import Platform
from src.game_object.video_tape import VideoTape
import src.game_object.actor as actor
from pytmx.util_pygame import load_pygame
import pygame
import src.graphics as graphics
import pyscroll
import src.logger as logger
import src.config as config

from src.tile_factory import TileFactory

class TiledMap():
    """
    @self.file = Tiled map filename
    @self._map = The TiledMap object of self.file
    @self.data = A sprite group of all of the tiles in self._map
    """
    def __init__(self, file, screen: pygame.Surface):
        self.tmx_file = file

        print(self.tmx_file)
        self._map = load_pygame(self.tmx_file)
        self.map_data_for_camera = pyscroll.TiledMapData(self._map)

        self.map_layer_for_camera = pyscroll.BufferedRenderer(
            self.map_data_for_camera,
            graphics.BASE_RESOLUTION
            # clamp_camera=False
        )

        self.sprites = pyscroll.PyscrollGroup(
            map_layer=self.map_layer_for_camera
        )

        # Used to keep a note of all solid tiles
        # handy for our moving laser code and saves iterating through
        # all the tiles at runtime for solid tiles
        self.solids = pygame.sprite.Group()

        self.paths = {}
        self.map_layer_for_camera.zoom = graphics.ZOOM_LEVEL

        self.properties = self._map.properties
        self.create_sprites_from_map()
        self.link_doors_and_switches()
        self.link_portals()

    def create_sprites_from_map(self):
        """Iterates through the TiledMap file adding tiles to
        the self.sprites sprite group
        """
        factory = TileFactory()

        try:
            for tile_object in self._map.get_layer_by_name('paths'):
                self.paths[tile_object.path_id] = Path(
                    tile_object.points, 
                    tile_object.path_id
                )
        except (AttributeError, ValueError):
            logger.LOGGER.info('Level "' + self.tmx_file + '" does not have a "paths" layer.')
        try:
            for tile_object in self._map.get_layer_by_name('objects'):
                surface = self._map.get_tile_image_by_gid(tile_object.gid)
                obj = self._create_tile(tile_object, surface, factory)
                self.sprites.add(obj)

                if isinstance(obj, SolidTile):
                    self.solids.add(obj)

        except ValueError:
            logger.LOGGER.info('Level "' + self.tmx_file + '" does not have a "objects" layer.')

    def _create_tile(self, tile_object, surface, factory):
        """Creates tiles passed to it. It finds the type of the
        tile_object and then creates the corresponding tile"""
        # Safe fallbacks just in case objects don't have certain attributes
        state = getattr(tile_object, 'state', 0)
        triggers = getattr(tile_object, 'triggers', False)
        triggered_id = getattr(tile_object, 'triggered_id', False)

        common = {
            'x': tile_object.x,
            'y': tile_object.y,
            'width': tile_object.width,
            'height': tile_object.height,
            'image': surface
        }

        if tile_object.type == 'particle_emitter':
            type_map = {
                'particle_emitter': {
                    'x': tile_object.x,
                    'y': tile_object.y,
                    'level': self,
                    'emits': tile_object.emits,
                }
            }

        if tile_object.type == 'moving_platform':
            type_map = {
                'moving_platform': {
                    **common,
                    'path': self.paths[tile_object.follows_path_id]
                }
            }

        if tile_object.type == 'platform':
            type_map = {
                'platform': {
                    **common,
                    'path': self.paths[tile_object.follows_path_id]
                }
            }

        if tile_object.type == 'video_tape':
            type_map = {
                'video_tape': {
                    **common,
                    'story': tile_object.properties.get('story', config.tape_dir + "first-tape")
                },
            }

        if tile_object.type == 'destructible':
            type_map = {
                'destructible': {
                    **common,
                },
            }

        if tile_object.type == 'portal':
            type_map = {
                'portal': {
                    **common,
                    'portal_id': tile_object.portal_id,
                    'travels_to_portal_id': tile_object.travels_to_portal_id
                },
            }

        if tile_object.type == 'pressure_plate':
            type_map = {
                'pressure_plate': {
                    **common,
                    'state': state,
                    'triggers': triggers,
                },
            }

        if tile_object.type == 'tile':
            type_map = {
                'tile': {
                    **common,
                },
            }

        if tile_object.type == 'actor':
            type_map = {
                'actor':{
                    **common,
                    'level': self,
                    'remaining_bombs': self.properties.get('player_bomb_count', 0),
                },
            }

        if tile_object.type == 'enemy_bombable':
            type_map = {
                'enemy_bombable':{
                    **common,
                    'path': self.paths[tile_object.follows_path_id]
                },
            }

        if tile_object.type == 'enemy_pathable':
            type_map = {
                'enemy_pathable':{
                    **common,
                    'path': self.paths[tile_object.follows_path_id],
                    'speed': tile_object.properties.get('speed', 2),
                },
            }

        if tile_object.type == 'laser_up':
            type_map = {
                'laser_up': {
                    **common,
                    'path': self.paths[tile_object.follows_path_id],
                    'level': self,
                    'direction': "up"
                },
            }

        if tile_object.type == 'laser_right':
            type_map = {
                'laser_right': {
                    **common,
                    'path': self.paths[tile_object.follows_path_id],
                    'level': self,
                    'direction': "right"
                },
            }

        if tile_object.type == 'tile':
            type_map = {
                'tile': {
                    **common,
                },
            }

        if tile_object.type == 'finish_tile':
            type_map = {
                'finish_tile': {
                    **common,
                },
            }

        if tile_object.type == 'scene_switching_tile':
            type_map = {
                'scene_switching_tile': {
                    **common,
                    'scene': tile_object.scene 
                },
            }

        if tile_object.type == 'pickup_bomb':
            type_map = {
                'pickup_bomb': {
                    **common
                },
            }

        if tile_object.type == 'bomb':
            type_map = {
                'bomb': {
                    **common,
                    'level': self,
                    'lifespan': tile_object.lifespan
                },
            }

        if tile_object.type == 'switch':
            type_map = {
                'switch': {
                    **common,
                    'state': state,
                    'triggers': triggers,
                },
            }

        # Barrels all use one class but pass a direction through
        if tile_object.type == 'barrel_down':
            type_map = {
                'barrel_down': {
                    'pattern': tile_object.properties.get('pattern', 'constant'),
                    **common,
                    'direction': 'down',
                    'bullet_speed': tile_object.properties.get('bullet_speed', 2),
                    'level': self,
                },
            }
        if tile_object.type == 'barrel_up':
            type_map = {
                'barrel_up': {
                    'pattern': tile_object.properties.get('pattern', 'constant'),
                    **common,
                    'direction': 'up',
                    'bullet_speed': tile_object.properties.get('bullet_speed', 2),
                    'level': self,
                },
            }

        if tile_object.type == 'barrel_right':
            type_map = {
                'barrel_right': {
                    'pattern': tile_object.properties.get('pattern', 'constant'),
                    **common,
                    'bullet_speed': tile_object.properties.get('bullet_speed', 2),
                    'direction': 'right',
                    'level': self,
                },
            }

        if tile_object.type == 'barrel_left':
            type_map = {
                'barrel_left': {
                    'pattern': tile_object.properties.get('pattern', 'constant'),
                    'bullet_speed': tile_object.properties.get('bullet_speed', 2),
                    **common,
                    'direction': 'left',
                    'level': self,
                },
            }

        if tile_object.type == 'barrel_down_left':
            type_map = {
                'barrel_down_left': {
                    'pattern': tile_object.properties.get('pattern', 'constant'),
                    **common,
                    'bullet_speed': tile_object.properties.get('bullet_speed', 2),
                    'direction': 'down_left',
                    'level': self,
                },
            }
        if tile_object.type == 'barrel_down_right':
            type_map = {
                'barrel_down_right': {
                    'pattern': tile_object.properties.get('pattern', 'constant'),
                    **common,
                    'bullet_speed': tile_object.properties.get('bullet_speed', 2),
                    'direction': 'down_right',
                    'level': self,
                },
            }

        if tile_object.type == 'barrel_up_left':
            type_map = {
                'barrel_up_left': {
                    'pattern': tile_object.properties.get('pattern', 'constant'),
                    **common,
                    'bullet_speed': tile_object.properties.get('bullet_speed', 2),
                    'direction': 'up_left',
                    'level': self,
                    'pattern': tile_object.properties.get('pattern', 'constant')
                },
            }

        if tile_object.type == 'barrel_up_right':
            type_map = {
                'barrel_up_right': {
                    'pattern': tile_object.properties.get('pattern', 'constant'),
                    'bullet_speed': tile_object.properties.get('bullet_speed', 2),
                    **common,
                    'direction': 'up_right',
                    'level': self,
                },
            }

        if tile_object.type == 'triggerable':
            type_map = {
                'triggerable': {
                    **common,
                    'stateful': 'pass',
                    'id': triggered_id,
                    'level': self
                },
            }

        if tile_object.type == 'moveable_tile':
            type_map = {
                'moveable_tile': {
                    **common,
                },
            }


        if tile_object.type == 'torch':
            type_map = {
                'torch': {
                    **common,
                },
            }


        if tile_object.type == 'door':
            type_map = {
                'door': {
                    **common,
                },
            }
        if tile_object.type == 'deadly_area':
            type_map = {
                'deadly_area': {
                    **common,
                },
            }

        if tile_object.type == 'computer_terminal':
            type_map = {
                'computer_terminal': {
                    **common, 
                    'minigame': tile_object.properties.get('minigame', './assets/levels/tmx/minigame-hunt'),
                    'state': 0,
                    'triggers': triggers,
                },
            }

        if tile_object.type == 'minigame-hunt-player':
            type_map = {
                'minigame-hunt-player': {
                    **common,
                },
            }

        if tile_object.type == 'minigame-hunt-collectible':
            type_map = {
                'minigame-hunt-collectible': {
                    **common,
                },
            }

        try:
            return factory.build(tile_object.type, **type_map[tile_object.type])
        except KeyError:
            logger.LOGGER.info('Invalid key "' + tile_object.type + '" passed to factory for level: ' + self.tmx_file)
        except UnboundLocalError:
            logger.LOGGER.info('Invalid key "' + tile_object.type + '" passed to factory for level: ' + self.tmx_file)

    def link_portals(self):
        """Makes sure that the switches are passed to the correct
           door object(Triggerable)"""
        for sprite in self.sprites:
            if isinstance(sprite, Portal):
                for other_sprite in self.sprites:
                    if isinstance(other_sprite, Portal):
                        if sprite.travels_to_portal_id == other_sprite.portal_id:
                            sprite.destination_portal = other_sprite

    def link_doors_and_switches(self):
        """Makes sure that the switches are passed to the correct
           door object(Triggerable)"""
        for state in self.sprites:
            if isinstance(state, Switch) or isinstance(state, PressurePlate):
                for trigger in self.sprites:
                    if isinstance(trigger, Triggerable):
                        if state.triggers == trigger.triggered_id:
                            trigger.stateful = state

    def get_tile_all_layers(self, x, y):
        """The same as get_tile but gets tiles at x, and y, on
        all layers instead of the first layer it sees to match
        the x and y"""
        return [tile for tile in self.sprites if tile.rect.x == x and tile.rect.y == y]

    def get_tile_from_object_layer(self, x, y):
        """Gets the tile from the object layer and then maps it to the one in the
        sprite group. This means we can kill our sprites etc..."""
        sprites = []
        for sprite in self.sprites:
            if sprite.rect.x == x and sprite.rect.y == y:
                sprites.append(sprite)
        return sprites

    def get_player(self, tiles):
        """Gets the player"""
        for tile in tiles:
            if isinstance(tile, actor.Actor):
                return tile

    def get_video_tape(self, tiles):
        """Gets the player"""
        for tile in tiles:
            if isinstance(tile, VideoTape):
                return tile

    def find_solid_tile(self, tiles):
        """Returns true if it finds a solid tile in a list of tiles"""
        for tile in tiles:
            if isinstance(tile, SolidTile):
                return tile
