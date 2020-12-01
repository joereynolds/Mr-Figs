"""
This is the thing that mr-figs can stand on and
be moved around on.
"""

import pygame
from src.game_object.path import Path
import src.entity as entity
import src.colours as colours

class Platform(entity.Entity):
    # TODO - Typehint path as Path
    def __init__(self, x, y, width, height, follows_path_id=None, path=None, image=None, ):
        entity.Entity.__init__(self, x, y, width, height, image)
        self.minimap_colour = colours.RED_HIGHLIGHT
        self.follows_path_id = follows_path_id
        self.follows_path = path

    def handle_collision(self, tile, player, level):
        if pygame.sprite.collide_rect(player, self):
            player.rect.x = self.follows_path.points[-1][0]
            player.rect.y = self.follows_path.points[-1][1]
            player.destination[0] = self.follows_path.points[-1][0]
            player.destination[1] = self.follows_path.points[-1][1]
