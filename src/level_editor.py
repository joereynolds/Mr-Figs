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
    def __init__(self, file, screen):
        self.tmx_file = file

        self._map = load_pygame(self.tmx_file)
        self.map_data_for_camera = pyscroll.TiledMapData(self._map)

        self.map_layer_for_camera = pyscroll.BufferedRenderer(
            self.map_data_for_camera,
            (100, 100)
        )

        self.map_layer_for_camera.zoom = 1

        self.sprites = pyscroll.PyscrollGroup(
            map_layer=self.map_layer_for_camera
        )

        self.tile_spacing = graphics.tile_width
        self.properties = self._map.properties
        self.get_map_data()
        self.link_doors_and_switches()

    def get_map_data(self):
        """Iterates through the TiledMap file adding tiles to
        the self.sprites sprite group
        @x =
        @y =
        @pix_x =
        @pix_y =
        """
        factory = TileFactory()
        for i, layer in enumerate(self._map):
            for _tile in layer.tiles():
                x, y, surface = _tile[0], _tile[1], _tile[2]
                current_tile = self._map.get_tile_properties(x, y, i)
                if current_tile:
                    scaled = graphics.scale_up(surface)
                    obj = self._create_tile(x, y, scaled, current_tile, factory)
                    self.sprites.add(obj, layer=i)

    def _create_tile(self, x, y, surface, sprite, factory):
        """Creates tiles passed to it. It finds the type of the
        sprite and then creates the corresponding tile"""
        x = x * self.tile_spacing
        y = y * self.tile_spacing

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
                'solid':sprite.get('solid'),
                'destructable':sprite.get('destructable'),
            },
            'actor':{
                **common,
                'level': self,
                'image':surface
            },
            'bomb': {
                **common,
                'level': self,
                'lifespan': sprite.get('lifespan'),
            },
            'pickup_bomb': {
                **common
            },
            'finish_tile': {
                **common,
                'solid':sprite.get('solid'),
                'destructable':sprite.get('destructable'),
            },
            'moveable_tile': {
                **common,
                'solid':sprite.get('solid'),
                'destructable':sprite.get('destructable'),
                'moveable':sprite.get('moveable', False),
            },
            'stateful': {
                **common,
                'solid':sprite.get('solid'),
                'destructable':sprite.get('destructable'),
                'state':0,
                'triggers':sprite.get('triggers'),
            },
            'triggerable': {
                **common,
                'solid':sprite.get('solid'),
                'destructable':sprite.get('destructable'),
                'stateful':'pass',
                'id':sprite.get('id')
            }
        }

        return factory.build(sprite.get('type'), **type_map[sprite.get('type')])

    def link_doors_and_switches(self):
        """Makes sure that the switches are passed to the correct
           door object(Triggerable)"""
        for state in self.sprites:
            if isinstance(state, tile.Stateful):
                for trigger in self.sprites:
                    if isinstance(trigger, tile.Triggerable):
                        if state.triggers == trigger.id:
                            trigger.stateful = state

    def get_tile(self,x,y):
        """Returns the tile object at @x and @y"""
        for tile in self.sprites:
            if tile.rect.x == x and tile.rect.y == y:
                return tile

    def get_tile_all_layers(self, x, y):
        """The same as get_tile but gets tiles at x, and y, on
        all layers instead of the first layer it sees to match
        the x and y"""
        return [tile for tile in self.sprites if tile.rect.x == x and tile.rect.y == y]

    def get_layer_count(self):
        """Returns the total count of layers.
        count starts at 1."""
        layers = [layer for layer in self._map]
        return len(layers)

    def get_tile_from_layer(self, x, y, layer):
        """The same as get_tile but returns the tile only from that layer"""
        for tile in self.sprites.get_sprites_from_layer(layer):
            if tile.rect.x == x and tile.rect.y == y:
                return tile

    def get_player(self, layer):
        """Returns the dummy player"""
        for _tile in self.sprites.get_sprites_from_layer(layer):
            if isinstance(tile, actor.Actor):
                return _tile

    def get_tiles_of_type(self, _type):
        """Returns all tiles from all layers that are an instance of type"""
        sprites = []
        for sprite in self.sprites:
            if isinstance(sprite, _type):
                sprites.append(sprite)
        return sprites

    def remove_dummy_player(self):
        """Takes the dummy player out of our group"""
        for tile in self.sprites:
            if isinstance(tile, actor.Actor):
                pygame.sprite.Sprite.kill(tile)

    #This function is gross and not needed. It's only used in the actor class and that could easily be a map over all
    #of the tiles. Do this asap
    def find_solid_tile(self, tiles):
        """Returns true if it finds a solid tile in a list of tiles"""
        for tile in tiles:
            if tile.solid:
                return tile
