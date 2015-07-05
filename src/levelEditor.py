import pygame
import random
import tile
import graphics
import actor


class Editor():

    """A dictionary containing attributes about each tile
       For example
       'X' : [True, True, path/to/img]
       
       'X' is the representation of the tile in the text file
        tile.Tile is the type of object to be created
        True Is whether the tile is solid or not
        True Is whether this tile can be destroyed via a bomb
        path/to/img is the path to the image if you have one
    """
    tiles = {'X' : [tile.Tile, True, False, graphics.ROCK_SPRITE],
             'O' : [tile.Tile, True, True, graphics.GOAL_SPRITE],
             '#' : [tile.Tile, False, False,graphics.FLOOR_SPRITE],
             'T' : [tile.Tile, True, True, graphics.TREE_SPRITE],
             'S' : [tile.Spike, False, False, graphics.SPIKEDOWN_SPRITE]
           }

    def __init__(self, _file):
        self.level = open(_file,'r')
        self.level_data = [line for line in self.level]
        self.created_level = pygame.sprite.Group() 
        self.make_level()

    def get_height(self):
        """Returns the total height of the level in pixels"""
        pass

    def get_width(self):
        """Returns the total width of the level in pixels"""
                    
    def get_tile(self,x,y):
        """Returns the tile at x,y position"""
        for tile in self.created_level:
            if tile.rect.x == x and tile.rect.y == y:
                return tile

    def make_level(self):
        """Converts our text file in objects and adds them to a sprite.Group"""
        #Go through each individual tile and check it against our tiles dict
        for y, tiles in enumerate(self.level_data):
            for x, _tile in enumerate(tiles):
                for tile_icon, attributes in Editor.tiles.items():
                    if _tile == tile_icon:
                        obj = Editor.tiles[_tile][0](x * 50,
                                        y * 50,
                                        50,
                                        50,
                                        Editor.tiles[_tile][1],
                                        Editor.tiles[_tile][2],
                                        Editor.tiles[_tile][3])
                        self.created_level.add(obj)
                       
