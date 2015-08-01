import pygame
import pytmx
import bomb
import tile
import graphics
import actor


class LevelData():

    def __init__(self, file):
        self.file = file
        self.tile_spacing = 48
        self._map = pytmx.TiledMap(self.file)
        self.data = pygame.sprite.LayeredUpdates()
        self.get_map_data()
        self.give_dynamic_sprites_data()

    def get_map_data(self):
        for i, layer in enumerate(self._map):
            for _tile in layer.tiles():
                x, y = _tile[0], _tile[1]
                pix_x, pix_y = _tile[2][1][0], _tile[2][1][1]
                surface = graphics.subsurf((pix_x, pix_y))

                current_tile = self._map.get_tile_properties(x,y,i)
                if current_tile:
                    obj = self._create_tile(x,y,surface,current_tile)
                    self.data.add(obj, layer=i)  

    def _create_tile(self,x,y,surface, attributes):
        x = x * self.tile_spacing
        y = y * self.tile_spacing
        if attributes['type'] == 'tile':
           _tile = tile.Tile(x,
                             y, 
                             self.tile_spacing, 
                             self.tile_spacing, 
                             solid=attributes['solid'], 
                             destructable=attributes['destructable'],
                             image=surface)

        if attributes['type'] == 'actor':
           _tile = self._create_player_tile(surface, x, y)
        if attributes['type'] == 'bomb':
           _tile = self._create_bomb_tile(surface, x, y)
        return _tile

    def _create_bomb_tile(self, surface, x, y):
        return bomb.Bomb(x, y, self.tile_spacing, self.tile_spacing,'pass', image=surface) 

    def _create_player_tile(self, surface, x, y):
        return actor.Actor(x , y, self.tile_spacing, self.tile_spacing, 'pass', image = surface) 

    def give_dynamic_sprites_data(self):
        """Once the map has been generated, go back and give the sprites
        that take a Level object the map data"""
        for sprite in self.data:
            if hasattr(sprite,'level'):
                sprite.level = self
    
    def get_tile(self,x,y):
        for tile in self.data:
            if tile.rect.x == x and tile.rect.y == y:
                return tile

    def get_tile_from_layer(self, x, y, layer):
        for tile in self.data.get_sprites_from_layer(layer):
            if tile.rect.x == x and tile.rect.y == y:
                return tile

    def get_player(self):
        """Returns the dummy player"""
        for tile in self.data:
            if isinstance(tile, actor.Actor):
                return tile

    def get_tiles_of_type(self, _type):
        """Returns all tiles from all layers that are an instance of type"""
        sprites = []
        for sprite in self.data:
            if isinstance(sprite, _type):
                sprites.append(sprite)
        return sprites 

    def remove_dummy_player(self):
        """Takes the dummy player out of our group"""
        for tile in self.data:
            if isinstance(tile, actor.Actor):
                print('killing player')
                pygame.sprite.Sprite.kill(tile)

mock = LevelData('../levels/tmx/new-level2.tmx')
#print(mock.get_player().rect.x)
#print(mock.get_player().rect.y)
#print(graphics.sprites['player']['sprites'][0])
