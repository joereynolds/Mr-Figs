"""
Constants pertaining to graphical use. Note that this can probably be moved to constants without too much bother.
"""
import pygame

WIDTH  = 700
HEIGHT = 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

spritesheet = pygame.image.load('../data/tiledsheet.png')

FLOOR_SPRITE     = spritesheet.subsurface(0,0,50,50)
TREE_SPRITE      = spritesheet.subsurface(50,0,50,50)
ROCK_SPRITE      = spritesheet.subsurface(100,0,50,50)
GOAL_SPRITE      = spritesheet.subsurface(150,0,50,50)
SPIKEDOWN_SPRITE = spritesheet.subsurface(200,0,50,50)
SPIKEUP_SPRITE   = spritesheet.subsurface(250,0,50,50)
BOMB_SPRITE      = spritesheet.subsurface(350,0,50,50)
