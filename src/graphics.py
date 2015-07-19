"""
Constants pertaining to graphical use. Note that this can probably be moved to constants without too much bother.
"""
import pygame

WIDTH  = 700
HEIGHT = 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

#sprite width, sprite height
sprite_width = 16 
sprite_height = 16
spritesheet = pygame.image.load('../data/newtiledsheet.png')


def subsurf(x, y):
    """Quick wrapper around pygame's subsurface so we don't keep having to pass in the width and height"""
    
    return spritesheet.subsurface(x, y, sprite_width, sprite_height)


ROCK_SPRITE  = subsurf(32,32)
FLOOR_SPRITE_1 = subsurf(0,48)
FLOOR_SPRITE_2 = subsurf(16,48)
ACTOR_SPRITE = subsurf(64,64)
