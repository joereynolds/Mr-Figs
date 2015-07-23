import pygame
import pytmx
import bomb
import random
import tile
import graphics
import actor
import csv

"""class TiledEditor():

    
    def __init__(self, map_csv):
        self.reader = csv.reader(map_csv)
        self.csv_data = self.get_data(map_csv)
        self.level_data = pygame.sprite.Group()
        self.spacing = graphics.trans_width
        self.make_level()
        self.player = self.get_player()

    def create_goal_tile(self, x, y, surface):
        return tile.Tile(x * self.spacing, y * self.spacing, graphics.sprite_width,graphics.sprite_height,True,True, surface)

    def create_destructable_tile(self,x,y,surface):
        return tile.Tile(x * self.spacing, y * self.spacing, graphics.sprite_width, graphics.sprite_height, True, True, surface)
    
    def create_solid_tile(self,x,y,surface):
        return tile.Tile(x * self.spacing, y * self.spacing, graphics.trans_width,graphics.trans_height,solid=True,destructable=False,image=surface)

    def create_stateful_tile(self,x,y,images,state):
        return tile.Stateful(x * self.spacing, y * self.spacing, graphics.trans_width, graphics.trans_height, False, False, state, images[state], images)

    def create_spike_tile(self, x, y, _state, surface):
        return tile.Spike(x * self.spacing, y * self.spacing, graphics.sprite_width, graphics.sprite_height, solid=False, destructable=False,state=_state, image=surface)

    def create_floor_tile(self,x,y,surface):
        return tile.Tile(x * self.spacing, y * self.spacing, graphics.sprite_width, graphics.sprite_height, False, False, surface)

    def create_finish_tile(self,x,y,surface):
        return tile.FinishTile(x * self.spacing, y* self.spacing, graphics.sprite_width, graphics.sprite_height, False, False, surface)

    def get_tile(self,x,y):
        for tile in self.level_data:
            if tile.rect.x == x and tile.rect.y == y:
                return tile

    def get_player(self):
        for tile in self.level_data:
            if isinstance(tile, actor.Actor):
                print(tile)
                return tile

    def get_data(self, map_csv):
        data = []
        with open(map_csv, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                if self.clean_row(row): #If we've purged the row of all crap and it's not empty then append it to our list
                    data.append(self.clean_row(row))
        return data

    def clean_row(self, row):
        try:
            row = row[:row.index('-1')]
        except ValueError:
            return
        return row

    def make_level(self):
        #Go through each individual tile and check it against our tiles dict
        for y, row in enumerate(self.csv_data):
            for x, cell in enumerate(row):
                for tile_icon, attributes in TiledEditor.tiles.items():
                    if cell == tile_icon:
                        tile_type = TiledEditor.tiles[cell][0]
                        tile_surface = TiledEditor.tiles[cell][-1]
 
                        if tile_type == 'solid':
                            obj = self.create_solid_tile(x,y, tile_surface)
                        elif tile_type == 'floor':
                            obj = self.create_floor_tile(x,y,tile_surface)
                        elif tile_type == 'state' :
                            obj = self.create_stateful_tile(x,y,TiledEditor.tiles[cell][2],TiledEditor.tiles[cell][1])
                        elif tile_type == 'destruct' :
                            obj = self.create_destructable_tile(x,y,tile_surface)
                        elif tile_type == 'goal':
                            obj = self.create_goal_tile(x,y,tile_surface)
                        elif tile_type == 'end':
                            obj = self.create_finish_tile(x,y,tile_surface)
                        self.level_data.add(obj)
"""

def get_map_data(tmx_file):
    """@tmx_file : A valid .tmx map file
    e.g.
        '../levels/tmx/level1.tmx' 
    """
    level_data = pygame.sprite.LayeredUpdates()
    map = pytmx.TiledMap(tmx_file)
    spacing = 48 #16 * 3 = 48 hence the number/Sprites are scaled up 3 times from 16x16
    for layer in map:
        for _tile in layer.tiles():
            x, y = _tile[0], _tile[1]
            pix_x = _tile[2][1][0]
            pix_y = _tile[2][1][1] 
            if (pix_x//16,pix_y//16) in graphics.SPRITES['wall']:
                _surface = graphics.subsurf((pix_x,pix_y))
                obj = tile.Tile(x * spacing, y *spacing, spacing, spacing, solid = True, destructable = False, image=_surface)
            elif (pix_x//16,pix_y//16) in graphics.SPRITES['floor']:
                _surface = graphics.subsurf((pix_x,pix_y))
                obj = tile.Tile(x * spacing, y *spacing, spacing, spacing, solid = False, destructable = False, image=_surface)
            elif (pix_x//16,pix_y//16) in graphics.SPRITES['rocks']:
                print('yES')
                _surface = graphics.subsurf((pix_x, pix_y))
                obj = tile.Tile(x * spacing, y *spacing, spacing, spacing, solid=True, destructable=True, image=_surface)
            level_data.add(obj) 
    return level_data

get_map_data('../levels/tmx/new-level1.tmx')
 


