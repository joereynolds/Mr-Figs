from src.game_object.switch_tile import Switch
from src.game_object.pressure_plate import PressurePlate
from src.game_object.triggerable import Triggerable
from src.game_object.portal import Portal
import src.game_object.actor as actor
from pprint import pprint
from pytmx.util_pygame import load_pygame
import pygame
import src.graphics as graphics
import pyscroll

from src.tile_factory import TileFactory

class LevelData():
    """
    @self.file = Tiled map filename
    @self.tile_spacing = The spacing between each tile when rendered
    @self._map = The TiledMap object of self.file
    @self.data = A sprite group of all of the tiles in self._map
    """
    def __init__(self, file, screen: pygame.Surface):
        self.tmx_file = file

        self._map = load_pygame(self.tmx_file)
        self.map_data_for_camera = pyscroll.TiledMapData(self._map)

        self.map_layer_for_camera = pyscroll.BufferedRenderer(
            self.map_data_for_camera,
            (100, 100),
        )

        self.sprites = pyscroll.PyscrollGroup(
            map_layer=self.map_layer_for_camera
        )

        # Would've thought .5 would make it smaller but actually makes it bigger?
        self.map_layer_for_camera.zoom = .5

        self.tile_spacing = graphics.tile_width
        self.properties = self._map.properties
        self.get_map_data()
        self.link_doors_and_switches()
        self.link_portals()

    def get_map_data(self):
        """Iterates through the TiledMap file adding tiles to
        the self.sprites sprite group
        """
        factory = TileFactory()
        
        try:
            for tile_object in self._map.get_layer_by_name('objects'):
                surface = self._map.get_tile_image_by_gid(tile_object.gid)
                obj = self._create_tile(tile_object, surface, factory)
                self.sprites.add(obj)
        except ValueError:
            print('this scene doesnt have objects')


    def _create_tile(self, tile_object, surface, factory):
        """Creates tiles passed to it. It finds the type of the
        tile_object and then creates the corresponding tile"""
        x = tile_object.x
        y = tile_object.y

        # Safe fallbacks just in case objects don't have certain attributes
        moveable = getattr(tile_object, 'moveable', False)
        state = getattr(tile_object, 'state', False)
        solid = getattr(tile_object, 'solid', False)
        destructable = getattr(tile_object, 'destructable', False)
        lifespan = getattr(tile_object, 'lifespan', False)
        triggers = getattr(tile_object, 'triggers', False)
        triggered_id = getattr(tile_object, 'triggered_id', False)
        portal_id = getattr(tile_object, 'portal_id', False)
        travels_to_portal_id = getattr(tile_object, 'travels_to_portal_id', False)

        common = {
            'x': x,
            'y': y,
            'width': self.tile_spacing,
            'height': self.tile_spacing,
            'image': surface
        }

        type_map = {
            'tile': {
                **common,
                'solid': solid,
                'destructable':destructable,
            },
            'actor':{
                **common,
                'level': self,
                'image':surface,
                'remaining_bombs': self.properties.get('player_bomb_count', 0),
            },
            'bomb': {
                **common,
                'level': self,
                'lifespan':lifespan,
            },
            'pickup_bomb': {
                **common
            },
            'finish_tile': {
                **common,
                'solid': solid,
                'destructable':destructable,
            },
            'moveable_tile': {
                **common,
                'solid': solid,
                'destructable':destructable,
                'moveable': moveable
            },
            'switch': {
                **common,
                'solid': solid,
                'destructable':destructable,
                'state': state,
                'triggers': triggers,
            },
            'pressure_plate': {
                **common,
                'solid': solid,
                'destructable':destructable,
                'state': state,
                'triggers': triggers,
                'images': graphics.sprites['pressure_plate']['sprites']
            },
            'triggerable': {
                **common,
                'solid': solid,
                'destructable':destructable,
                'stateful':'pass',
                'id': triggered_id
            },
            'portal': {
                **common,
                'portal_id': portal_id,
                'travels_to_portal_id': travels_to_portal_id
            },
            'video_tape': {
                **common,
            },
            'hole': {
                **common,
                'solid': solid,
                'destructable':destructable,
            }
        }

        try:
            return factory.build(tile_object.type, **type_map[tile_object.type])
        except KeyError:
            print('You passed an invalid key to the factory for level: ' + self.tmx_file)

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
        for sprite in self.sprites:
            if sprite.rect.x == x and sprite.rect.y == y:
                return sprite

    def get_player(self, tiles):
        """Returns true if it finds a solid tile in a list of tiles"""
        for tile in tiles:
            if isinstance(tile, actor.Actor):
                return tile

    def find_solid_tile(self, tiles):
        """Returns true if it finds a solid tile in a list of tiles"""
        for tile in tiles:
            if tile.solid:
                return tile
