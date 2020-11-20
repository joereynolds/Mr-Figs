import pygame

from src.game_object.switch_tile import Switch
import src.game_object.tile as tile
import src.entity as entity
import src.colours as colours
import src.graphics as graphics

class Hole(tile.Tile):
    """
    A hole for the player to fall down
    """
    def __init__(self, x, y, width, height, solid, destructable, image):
        tile.Tile.__init__(self, x, y, width, height, solid, destructable, image)
        self.minimap_colour = colours.BLACK

    def handle_collision(self, tile, player, level):
        for _tile in level.tiled_level.sprites:
            if hasattr(_tile, 'destination'):
                if _tile.destination[0] == self.rect.x and _tile.destination[1] == self.rect.y:
                    pygame.sprite.Sprite.kill(_tile)
                    return True
