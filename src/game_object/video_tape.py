import pygame

import src.colours as colours
from src.entity import Entity

class VideoTape(Entity):
    """The tile class represents any tile in the game background,
        or foreground.
        It extends the entity class
        to add collision mechanics and various other bits"""

    def __init__(self, x, y, width, height, image=None):
        Entity.__init__(self, x, y, width, height, image)

        self.minimap_colour = colours.WHITE

    def handle_collision(self, tile, player, level):
        if player.destination[0] == self.rect.x and player.destination[1] == self.rect.y:
            pygame.sprite.Sprite.kill(self)
