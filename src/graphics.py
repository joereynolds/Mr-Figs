import pygame

WIDTH  = 700
HEIGHT = 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

sprite_width = 16 
sprite_height = 16
spritesheet = pygame.image.load('../data/newtiledsheet.png')

trans_width = 48
trans_height = 48

def grid(x,y):
    """Returns the sprite at the gridded position of n m rather than having to work out the time table for sprite widths!"""
    return sprite_width * x, sprite_height * y 


def subsurf(grid_pos):
    """Quick wrapper around pygame's subsurface so we don't keep having to pass in the width and height"""
    surface = spritesheet.subsurface(grid_pos[0], grid_pos[1], sprite_width, sprite_height) 
    return pygame.transform.scale(surface, (trans_width, trans_height)) 


ACTOR_SPRITE   = subsurf(grid(0,5))

BOMB_SPRITE_5  = subsurf(grid(0,4))
BOMB_SPRITE_4  = subsurf(grid(1,4))
BOMB_SPRITE_3  = subsurf(grid(2,4))
BOMB_SPRITE_2  = subsurf(grid(3,4))
BOMB_SPRITE_1  = subsurf(grid(4,4))
BOMB_SPRITE_OFF= subsurf(grid(5,4))

LASER_ON       = subsurf(grid(5,1))
LASER_OFF      = subsurf(grid(4,1))
LASER_PULSE    = subsurf(grid(6,1))
LASER_PULSE_HARD = subsurf(grid(7,1))
LASER_IMAGES   = [LASER_OFF, LASER_ON, LASER_PULSE, LASER_PULSE_HARD]


"""

Note that you can't check membership in a tuple if there's only one element (wtf?)

So this:
    if (2,2) in ((2,2))
Doesn't work.
But
    if (2,2) in ((2,2),(2,2))
Does...
"""
SPRITES = {
           'wall'   : ((0,1),(0,0),(1,0),(1,1),
                       (2,0),(3,0),(2,1),(3,1),
                       (2,3),(1,3),(0,3)),
           'floor'  : ((1,2),(0,2)),
           'bombs'   : ((0,4),(1,4),(2,4),(3,4),(4,4),(5,4)),
           'stairs' : ((5,3),),
           'rocks'  : ((2,2),)
           }
