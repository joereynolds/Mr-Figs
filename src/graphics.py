import pygame

WIDTH  = 700
HEIGHT = 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

#sprite width, sprite height
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


ROCK_SPRITE    = subsurf(grid(2,2))
FLOOR_SPRITE_1 = subsurf(grid(1,2))
FLOOR_SPRITE_2 = subsurf(grid(0,2))
ACTOR_SPRITE   = subsurf(grid(0,5))
BOMB_SPRITE    = subsurf(grid(0,4))
WALL_UP        = subsurf(grid(0,1))
WALL_DOWN      = subsurf(grid(0,0))
WALL_RIGHT     = subsurf(grid(1,1))
STAIRS         = subsurf(grid(3,5))

for i in range(0,400,16):
    print(i)
