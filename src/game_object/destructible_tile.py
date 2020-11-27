import src.colours as colours
from src.game_object.tile import Tile
import src.environment

class Destructible(Tile):
    def __init__(self, x, y, width, height, image=None):
        Tile.__init__(self, x, y, width, height, True, image)
        self.minimap_colour = colours.BROWN_HIGHLIGHT
