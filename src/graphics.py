"""
Constants pertaining to graphical use. Note that this can probably be moved to constants without too much bother.
"""
import pygame

WIDTH  = 700
HEIGHT = 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

spritesheet = pygame.image.load('../data/tiledsheet.png')
lspritesheet = pygame.image.load('../data/ltiledsheet.png')

#ROCK SPRITES

ROCK_STANDALONE_SPRITE          = lspritesheet.subsurface(100,0,50,50)
ROCK_CORNER_TOP_LEFT_SPRITE     = lspritesheet.subsurface(0,50,50,50)
ROCK_CORNER_TOP_MID_SPRITE      = lspritesheet.subsurface(100,0,50,50)
ROCK_CORNER_TOP_RIGHT_SPRITE    = lspritesheet.subsurface(100,0,50,50)
ROCK_CORNER_BOTTOM_LEFT_SPRITE  = lspritesheet.subsurface(0,150,50,50)
ROCK_CORNER_BOTTOM_MID_SPRITE   = lspritesheet.subsurface(50,150,50,50)
ROCK_CORNER_BOTTOM_RIGHT_SPRITE = lspritesheet.subsurface(100,0,50,50)
ROCK_SURROUNDED_SPRITE          = lspritesheet.subsurface(100,0,50,50)
ROCK_PATH_TOP_SPRITE            = lspritesheet.subsurface(100,0,50,50)
ROCK_PATH_BOTTOM_SPRITE         = lspritesheet.subsurface(100,0,50,50)
ROCK_PATH_LEFT_SPRITE           = lspritesheet.subsurface(100,0,50,50)
ROCK_PATH_RIGHT_SPRITE          = lspritesheet.subsurface(100,0,50,50)

FLOOR_SPRITE     = lspritesheet.subsurface(0,0,50,50)
TREE_SPRITE      = lspritesheet.subsurface(50,0,50,50)
GOAL_SPRITE      = spritesheet.subsurface(150,0,50,50)
SPIKEDOWN_SPRITE = spritesheet.subsurface(200,0,50,50)
SPIKEMID_SPRITE  = spritesheet.subsurface(250,0,50,50)
SPIKEUP_SPRITE   = spritesheet.subsurface(300,0,50,50)
BOMB_SPRITE      = spritesheet.subsurface(400,0,50,50)
ACTOR_SPRITE     = spritesheet.subsurface(450,0,50,50)
FINISHED_SPRITE  = spritesheet.subsurface(500,0,50,50)
