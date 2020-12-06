import pygame
from src.entity import Entity
from typing import Tuple

"""
TODO - This shouldn't really be a sprite
it's just data that a platform or monster can follow.

It's been made a sprite since the PyscrollGroup expects sprites
when adding to it.

We could create a separate layer in Tiled and work with that, we'll see.
"""
class Path():
    
    def __init__(self, points: Tuple[int, int], id: int):
        self.id = id
        self.points = points
