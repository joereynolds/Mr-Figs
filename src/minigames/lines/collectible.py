import pygame
from src.entity import Entity

class Collectible(Entity):

    def __init__(
            self, 
            x: int, 
            y: int, 
            width: int, 
            height: int, 
            player_teleports_to_grid_x,
            player_teleports_to_grid_y,
            image=None
        ):
        Entity.__init__(self, x, y, width, height, image)
        self.player_teleports_to_grid_x = player_teleports_to_grid_x
        self.player_teleports_to_grid_y = player_teleports_to_grid_y
