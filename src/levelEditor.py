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

    def get_map_data(self):
        for layer in self._map:
            for _tile in layer.tiles():
                x, y = _tile[0], _tile[1]
                pix_x, pix_y = _tile[2][1][0], _tile[2][1][1]
                grid_x, grid_y = pix_x //16, pix_y//16
                surface = graphics.subsurf((pix_x, pix_y))
                if (grid_x, grid_y) in graphics.sprites['wall']['coords']:
                    obj = self.create_tile('wall', surface, x, y)
                elif (grid_x, grid_y) in graphics.sprites['floor']['coords']:
                    obj = self.create_tile('floor', surface, x, y)
                elif (grid_x, grid_y) in graphics.sprites['rock']['coords']:
                    obj = self.create_tile('rock', surface, x, y)
                elif (grid_x, grid_y) in graphics.sprites['player']['coords']:
                    obj = self.create_tile('player', surface, x, y)
                self.data.add(obj) 

    def create_tile(self, sprite_type, surface, x, y):
        if sprite_type == 'wall'  :
            tile = self._create_wall_tile(surface, x, y)
        if sprite_type == 'floor' :
            tile = self._create_floor_tile(surface, x, y)
        if sprite_type == 'rock' :
            tile = self._create_rock_tile(surface, x, y)
        if sprite_type == 'player':
            tile = self._create_player_tile(surface, x, y)
        return tile
    
    def _create_player_tile(self, surface, x, y):
        pass

    def _create_wall_tile(self, surface, x, y):
        return tile.Tile(x * self.tile_spacing, y * self.tile_spacing, self.tile_spacing, self.tile_spacing, solid = True, destructable = False, image=surface)

    def _create_floor_tile(self, surface, x, y):
        return tile.Tile(x * self.tile_spacing, y * self.tile_spacing, self.tile_spacing, self.tile_spacing, solid = False, destructable = False, image=surface)

    def _create_rock_tile(self, surface, x, y):
        return tile.Tile(x * self.tile_spacing, y * self.tile_spacing, self.tile_spacing, self.tile_spacing, solid=True, destructable=True, image=surface)
    
    def get_tile(self,x,y):
        for tile in self.data:
            if tile.rect.x == x and tile.rect.y == y:
                return tile

    def get_player(self):
        for tile in self.data:
            if isinstance(tile, actor.Actor):
                return tile

mock = LevelData('../levels/tmx/new-level1.tmx')
mock.get_player()
