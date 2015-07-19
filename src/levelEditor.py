import pygame
import bomb
import random
import tile
import graphics
import actor
import csv

class TiledEditor():
    """This class is designed to work with the CSV files passed on from the Tiled program"""

    """A dictionary containing attributes about each tile
       For example
       '0' : [tile.Tile,True, True, path/to/img]
       
       '0' is the representation of the tile in the Tiled csv file
        tile.Tile is the type of object to be created
        True Is whether the tile is solid or not
        True Is whether this tile can be destroyed via a bomb
        path/to/img is the path to the image if you have one
    """
    tiles = {
             '32' : ['end', graphics.STAIRS], 
             '29' : ['solid', graphics.WALL_LOWER_RIGHT],
             '28' : ['solid', graphics.WALL_UPPER_LEFT],
             '27' : ['solid', graphics.WALL_UPPER_RIGHT],
             '20' : ['destruct', graphics.ROCK_SPRITE],
             '19' : ['floor', graphics.FLOOR_SPRITE_1],
             '18' : ['floor', graphics.FLOOR_SPRITE_2],
             '14' : ['state',1,graphics.LASER_IMAGES, graphics.LASER_ON],
             '13' : ['state',0,graphics.LASER_IMAGES, graphics.LASER_OFF],
             '2' : ['solid', graphics.WALL_DOWN_RIGHT],
             '3'   : ['solid', graphics.WALL_DOWN_LEFT],
             '12' : ['solid' , graphics.WALL_UP_LEFT],
             '11' : ['solid', graphics.WALL_UP_RIGHT],
             '10' : ['solid' , graphics.WALL_RIGHT],
             '9'  : ['solid' , graphics.WALL_UP],
             '0'  : ['solid' , graphics.WALL_DOWN],
             '1'  : ['solid' , graphics.WALL_LEFT]
           }
    
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
        """Convenience function to shorten the make_level() function"""
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
        """Returns the tile at x,y position"""
        for tile in self.level_data:
            if tile.rect.x == x and tile.rect.y == y:
                return tile

    def get_player(self):
        """Returns the player instance present in the level data. This is used to pass to the Scene so that we can update our character as usual"""
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
        """Removes anything after a -1 in the row of the CSV.
        A -1 is Tiled's way of denoting that there is no tile present here.
        In this case we want to remove every -1"""
        try:
            row = row[:row.index('-1')]
        except ValueError:
            return
        return row

    def make_level(self):
        """Converts our csv data into objects and adds them to a sprite.Group"""
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
