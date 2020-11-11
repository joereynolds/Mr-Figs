import src.bomb as bomb
import src.tile as tile
import src.actor as actor
import pytmx
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

    def get_map_data(self):
        """Iterates through the TiledMap file adding tiles to
        the self.sprites sprite group
        """
        factory = TileFactory()
        
        try:
            for tile_object in self._map.get_layer_by_name('objects'):
                surface = self._map.get_tile_image_by_gid(tile_object.gid)
                obj = self._create_tile(tile_object, surface, tile_object, factory)
                self.sprites.add(obj)
        except ValueError:
            print('this scene doesnt have objects')

    def _create_tile(self, tile_object, surface, sprite, factory):
        """Creates tiles passed to it. It finds the type of the
        sprite and then creates the corresponding tile"""
        x = tile_object.x
        y = tile_object.y

        # Safe fallbacks just in case objects don't have certain attributes
        moveable = False
        if hasattr(sprite, 'moveable'):
            moveable = sprite.moveable

        solid = False
        if hasattr(sprite, 'solid'):
            solid = sprite.solid

        destructable = False
        if hasattr(sprite, 'destructable'):
            destructable = sprite.destructable

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
                'image':surface
            },
            # 'bomb': {
            #     **common,
            #     'level': self,
            #     'lifespan': sprite.lifespan,
            # },
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
            # 'stateful': {
            #     **common,
            #     'solid':sprite.solid,
            #     'destructable':destructable,
            #     'state':0,
            #     'triggers':sprite.triggers,
            # },
            'triggerable': {
                **common,
                'solid': solid,
                'destructable':destructable,
                'stateful':'pass',
                'id':sprite.id
            }
        }

        return factory.build(sprite.type, **type_map[sprite.type])

    def link_doors_and_switches(self):
        """Makes sure that the switches are passed to the correct
           door object(Triggerable)"""
        for state in self.sprites:
            if isinstance(state, tile.Stateful):
                for trigger in self.sprites:
                    if isinstance(trigger, tile.Triggerable):
                        if state.triggers == trigger.id:
                            trigger.stateful = state

    def get_tile_all_layers(self, x, y):
        """The same as get_tile but gets tiles at x, and y, on
        all layers instead of the first layer it sees to match
        the x and y"""
        return [tile for tile in self.sprites if tile.rect.x == x and tile.rect.y == y]

    def get_tile_from_layer(self, x, y, layer):
        """The same as get_tile but returns the tile only from that layer"""
        for tile in self.sprites.get_sprites_from_layer(layer):
            if tile.rect.x == x and tile.rect.y == y:
                return tile

    def get_tile_from_object_layer(self, x, y, layer_name='objects'):
        for tile in self._map.get_layer_by_name(layer_name):
            if tile.x == x and tile.y == y:
                return tile

    #This function is gross and not needed. It's only used in the actor class and that could easily be a map over all
    #of the tiles. Do this asap
    def find_solid_tile(self, tiles):
        """Returns true if it finds a solid tile in a list of tiles"""
        for tile in tiles:
            if tile.solid:
                return tile
