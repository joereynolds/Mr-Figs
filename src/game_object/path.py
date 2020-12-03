import pygame
from src.entity import Entity

"""
TODO - This shouldn't really be a sprite
it's just data that a platform or monster can follow.

It's been made a sprite since the PyscrollGroup expects sprites
when adding to it.

We could create a separate layer in Tiled and work with that, we'll see.
"""
class Path():
    
    def __init__(self, x, y, points, id):
        self.x = x
        self.y = y
        self.points = points
        self.id = id
