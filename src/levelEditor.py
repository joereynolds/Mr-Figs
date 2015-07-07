import pygame
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
             '0' : [tile.Tile, False, False,graphics.FLOOR_SPRITE],
             '1' : [tile.Tile, True, True, graphics.TREE_SPRITE],
             '2' : [tile.Tile, True, False, graphics.ROCK_SPRITE],
             '3' : [tile.Tile, True, True, graphics.GOAL_SPRITE],
             '4' : [tile.Spike, False, False, 0, graphics.SPIKEDOWN_SPRITE],
             '5' : [tile.Spike, False, False, 1, graphics.SPIKEUP_SPRITE],
             '9' : [tile.FinishTile, False, False, graphics.FINISHED_SPRITE]
           }
    
    def __init__(self, map_csv):
        self.reader = csv.reader(map_csv)
        self.csv_data = self.get_data(map_csv)
        self.level_data = pygame.sprite.Group()
        self.make_level()

    def get_tile(self,x,y):
        """Returns the tile at x,y position"""
        for tile in self.level_data:
            if tile.rect.x == x and tile.rect.y == y:
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
                        if TiledEditor.tiles[cell][0] == tile.Spike:
                            obj = TiledEditor.tiles[cell][0](x * 50,
                                            y * 50,
                                            50,
                                            50,
                                            TiledEditor.tiles[cell][1],
                                            TiledEditor.tiles[cell][2],
                                            TiledEditor.tiles[cell][3],
                                            TiledEditor.tiles[cell][4])
                        elif TiledEditor.tiles[cell][0] == tile.FinishTile:
                            obj = TiledEditor.tiles[cell][0](x * 50,
                                            y * 50,
                                            50,
                                            50,
                                            TiledEditor.tiles[cell][1],
                                            TiledEditor.tiles[cell][2],
                                            TiledEditor.tiles[cell][3])
                        else:
                            obj = TiledEditor.tiles[cell][0](x * 50,
                                            y * 50,
                                            50,
                                            50,
                                            TiledEditor.tiles[cell][1],
                                            TiledEditor.tiles[cell][2],
                                            TiledEditor.tiles[cell][3])
                        self.level_data.add(obj)
