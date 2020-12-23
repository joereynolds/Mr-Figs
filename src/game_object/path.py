import pygame
from src.entity import Entity
from typing import Tuple

class Path():
    
    def __init__(self, points: Tuple[int, int], id: int):
        self.id = id
        self.points = points
