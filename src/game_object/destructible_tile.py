import src.colours as colours
from src.game_object.solid_tile import SolidTile

class Destructible(SolidTile):
    def __init__(self, x, y, width, height, image=None):
        SolidTile.__init__(self, x, y, width, height, image)
        self.minimap_colour = colours.BROWN_HIGHLIGHT

    def handle_pre_bomb_particle_creation(self, level):
        return None

    def handle_post_bomb_particle_creation(self, level):
        level.sprites.remove(self)
