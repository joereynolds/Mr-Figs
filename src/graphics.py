import pygame
import src.config as config

#TODO this file is disgusting
sprite_width = 16
sprite_height = 16
spritesheet = pygame.image.load(config.spritesheet_location)

#scaled width and height
tile_width = 16
tile_height = 16

def get_window_surface():
    return pygame.display.set_mode((config.screen_width, config.screen_height))

def grid(x, y):
    """
    Returns the sprite at the gridded position of n m rather
    than having to work out the time table for sprite widths!
    """
    return sprite_width * x, sprite_height * y

def tile_grid(x, y):
    """
    Returns the sprite at the gridded position of n m rather
    than having to work out the time table for sprite widths!
    """
    return tile_width * x, tile_height * y


def subsurf(grid_pos):
    """
    Quick wrapper around pygame's subsurface so we don't keep having to pass in the width and height
    """
    surface = spritesheet.subsurface(grid_pos[0], grid_pos[1], sprite_width, sprite_height)
    return pygame.transform.scale(surface, (tile_width, tile_height))

def scale_up(surface):
    return pygame.transform.scale(surface, (tile_width, tile_height))


"""A dictionary of sprites and their properties
    coords = Their location on the spritesheet
    sprites = pygame surfaces of their location

"""
#TODO this should be moved to the editor? Or maye a SpriteMap class
sprites = {
    'wall'   : {
        'coords' : (
            (0,1),(0,0),(1,0),
            (1,1),(2,0),(3,0),
            (2,1),(3,1),(2,3),
            (1,3),(0,3)
        ),
    },
    'floor'  : {
        'coords'  : ((1,2),(0,2)),
        'sprite_1': subsurf(grid(1,2)),
        'sprite_2': subsurf(grid(0,2))
    },
    'bomb'  : {
        'coords'  : (
            (0,4),(1,4),(2,4),
            (3,4),(4,4),(5,4)
        ),
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
        'coords' : (),
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
    'rock'  : {
        'coords' : ((2,2),)
    },
    'player': {
        'coords' : ((0, 5),),
        'sprites':[subsurf(grid(0,5))]
    },
    'laser' : {
        'coords' : ((4, 1), (5, 1), (6, 1), (7, 1)),
        'sprites': [
            subsurf(grid(4, 1)),
            subsurf(grid(5, 1)),
            subsurf(grid(6, 1)),
            subsurf(grid(7, 1))
        ]
    },
    'switch': {
        'coords' : ((6, 3), (7, 3)),
        'sprites': [subsurf(grid(6, 3)),
                    subsurf(grid(7, 3))]
    }
}
