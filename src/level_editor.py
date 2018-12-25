import src.bomb as bomb
import src.tile as tile
import src.actor as actor
import pytmx
import pygame
import src.graphics as graphics


class LevelData():
    """
    @self.file = Tiled map filename
    @self.tile_spacing = The spacing between each tile when rendered
    @self._map = The TiledMap object of self.file
    @self.data = A sprite group of all of the tiles in self._map
    """
    def __init__(self, file):
        self.tmx_file = file
        self.tile_spacing = 48
        self._map = pytmx.TiledMap(self.tmx_file)
        self.sprites = pygame.sprite.LayeredUpdates()
        self.get_map_data()
        self.give_dynamic_sprites_data()
        self.link_doors_and_switches()

    def get_map_data(self):
        """Iterates through the TiledMap file adding tiles to
        the self.sprites sprite group
        @x =
        @y =
        @pix_x =
        @pix_y =
        """
        for i, layer in enumerate(self._map):
            for _tile in layer.tiles():
                x, y = _tile[0], _tile[1]
                pix_x, pix_y = _tile[2][1][0], _tile[2][1][1]
                surface = graphics.subsurf((pix_x, pix_y))

                current_tile = self._map.get_tile_properties(x,y,i)
                if current_tile:
                    obj = self._create_tile(x,y,surface,current_tile)
                    self.sprites.add(obj, layer=i)

    def _create_tile(self, x, y, surface, sprite):
        """Creates tiles passed to it. It finds the type of the
        sprite and then creates the corresponding tile"""
        x = x * self.tile_spacing
        y = y * self.tile_spacing
        if sprite['type'] == 'tile':
            _tile = self._create_standard_tile(x, y, sprite['solid'], sprite['destructable'], surface)
        elif sprite['type'] == 'actor':
           _tile = self._create_player_tile(surface, x, y)
        elif sprite['type'] == 'bomb':
           _tile = self._create_bomb_tile(sprite['lifespan'], surface, x, y)
        elif sprite['type'] == 'finish_tile':
            print('creating')
            _tile = self._create_finish_tile(x, y, sprite['solid'], sprite['destructable'], surface)
        elif sprite['type'] == 'stateful':
            _tile = self._create_stateful_tile(x, y, sprite['solid'], sprite['destructable'], surface, sprite['triggers'] )
        elif sprite['type'] == 'triggerable':
            _tile = self._create_triggerable_tile(x, y, sprite['solid'], sprite['destructable'],'pass', surface, sprite['id'])
        return _tile

    def link_doors_and_switches(self):
        """Makes sure that the switches are passed to the correct
           door object(Triggerable)"""
        for state in self.sprites:
            if isinstance(state, tile.Stateful):
                for trigger in self.sprites:
                    if isinstance(trigger, tile.Triggerable):
                        if state.triggers == trigger.id:
                            trigger.stateful = state
                            #much nest

    def _create_standard_tile(self, x, y, solid, destructable, surface):
        return tile.Tile(
           x, y,
           self.tile_spacing,
           self.tile_spacing,
           solid,
           destructable,
           surface
       )

    def _create_stateful_tile(self, x, y, solid, destructable, surface, triggers):
       return tile.Stateful(
          x, y,
          self.tile_spacing,
          self.tile_spacing,
          solid,
          destructable,
          0,
          surface,
          triggers
       )

    def _create_triggerable_tile(self, x, y, solid, destructable, stateful, surface, id):
        return tile.Triggerable(
            x,
            y,
            self.tile_spacing,
            self.tile_spacing,
            solid,
            destructable,
            stateful,
            surface,
            id
        )

    def _create_bomb_tile(self, lifespan, surface, x, y):
        return bomb.Bomb(
            x, y,
            self.tile_spacing,
            self.tile_spacing,
            'pass',
            lifespan,
            image = surface
        )

    def _create_player_tile(self, surface, x, y):
        return actor.Actor(
            x, y,
            self.tile_spacing,
            self.tile_spacing,
            'pass',
            image = surface
        )

    def _create_finish_tile(self, x, y, solid, destructable, surface):
        return tile.FinishTile(
           x, y,
           self.tile_spacing,
           self.tile_spacing,
           solid,
           destructable,
           surface
       )

    def give_dynamic_sprites_data(self):
        """Once the map has been generated, go back and give the sprites
        that take a Level object the map data"""
        for sprite in self.sprites:
            if hasattr(sprite,'level'):
                sprite.level = self

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
                return True
