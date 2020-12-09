import src.entity as entity
import src.environment
import src.colours as colours
from src.game_object.light_source import LightSource

class Torch(entity.Entity):
    def __init__(self, x, y, width, height, image=None):
        entity.Entity.__init__(self, x, y, width, height, image)
        self.minimap_colour = colours.RED
        self.light_mask = LightSource()

