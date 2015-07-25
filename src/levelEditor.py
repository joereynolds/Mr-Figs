import pygame
import pytmx
import bomb
import tile
import graphics
import actor


class LevelData():

    def __init__(self, file):
        self.file = file
        self._map = pytmx.TiledMap(self.file)
        self.data = pygame.sprite.LayeredUpdates()
        self.get_map_data()

    def get_map_data(self):
        spacing = 48 #16 * 3 = 48 hence the number/Sprites are scaled up 3 times from 16x16
        for layer in self._map:
            for _tile in layer.tiles():
                x, y = _tile[0], _tile[1]
                pix_x = _tile[2][1][0]
                pix_y = _tile[2][1][1] 
                grid_x = pix_x //16
                grid_y = pix_y //16
                if (grid_x, grid_y) in graphics.SPRITES['wall']['coords']:
                    _surface = graphics.subsurf((pix_x,pix_y))
                    obj = tile.Tile(x * spacing, y *spacing, spacing, spacing, solid = True, destructable = False, image=_surface)
                elif (grid_x, grid_y) in graphics.SPRITES['floor']['coords']:
                     _surface = graphics.subsurf((pix_x,pix_y))
                     obj = tile.Tile(x * spacing, y *spacing, spacing, spacing, solid = False, destructable = False, image=_surface)
                elif (grid_x, grid_y) in graphics.SPRITES['rocks']['coords']:
                    _surface = graphics.subsurf((pix_x, pix_y))
                    obj = tile.Tile(x * spacing, y *spacing, spacing, spacing, solid=True, destructable=True, image=_surface)
                self.data.add(obj) 

    def get_tile(self,x,y):
        for tile in self.data:
            if tile.rect.x == x and tile.rect.y == y:
                return tile

    def get_player(self):
        for tile in self.data:
            if isinstance(tile, actor.Actor):
                return tile

mock = LevelData('../levels/tmx/new-level1.tmx')

