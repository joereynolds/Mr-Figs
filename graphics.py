import pygame

WIDTH  = 700
HEIGHT = 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

spritesheet = pygame.image.load('data/spritesheet.png')

ROCK_SPRITE      = spritesheet.subsurface(166,245,50,50)
GOAL_SPRITE      = spritesheet.subsurface(509,217,50,50)
TREE_SPRITE      = spritesheet.subsurface(378,241,50,50)
FLOOR_SPRITE     = spritesheet.subsurface(466,68,50,50)
SPIKEUP_SPRITE   = spritesheet.subsurface(611,295,50,50)
SPIKEDOWN_SPRITE = spritesheet.subsurface(608,214,50,50)
