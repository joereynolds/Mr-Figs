import pygame
import src.config as config

#TODO this file is disgusting
spritesheet = pygame.image.load(config.spritesheet_location)

tile_width = 16
tile_height = 16

def get_window_surface():
    return pygame.display.set_mode((config.screen_width, config.screen_height))

def grid(x, y):
    """
    Returns the sprite at the gridded position of n m rather
    than having to work out the time table for sprite widths!
    """
    return tile_width * x, tile_height * y

def subsurf(grid_pos):
    """
    Quick wrapper around pygame's subsurface so we don't keep having to pass in the width and height
    """
    return spritesheet.subsurface(grid_pos[0], grid_pos[1], tile_width, tile_height)


"""A dictionary of sprites and their properties
    sprites = pygame surfaces of their location
"""
#TODO this should be moved to the editor? Or maye a SpriteMap class
sprites = {
    'floor'  : {
        'sprite_1': subsurf(grid(1,2)),
        'sprite_2': subsurf(grid(0,2))
    },
    'bomb'  : {
        'sprites' : [
            subsurf(grid(0,4)),
            subsurf(grid(1,4)),
            subsurf(grid(2,4)),
            subsurf(grid(3,4)),
            subsurf(grid(4,4)),
            subsurf(grid(5,4))
        ]
    },
    'explosion' :{
        'sprites':[
            subsurf(grid(0, 6)),
            subsurf(grid(1, 6)),
            subsurf(grid(2, 6)),
            subsurf(grid(3, 6)),
            subsurf(grid(4, 6)),
            subsurf(grid(5, 6))
        ]
    },
    'stair' : {
        'sprite_1' : subsurf(grid(5,3)),
    },
    'player': {
        'sprites':[subsurf(grid(0,5))]
    },
    'laser' : {
        'sprites': [
            subsurf(grid(4, 1)),
            subsurf(grid(5, 1)),
            subsurf(grid(6, 1)),
            subsurf(grid(7, 1))
        ]
    },
    'switch': {
        'sprites': [subsurf(grid(6, 3)),
                    subsurf(grid(7, 3))]
    }
}
