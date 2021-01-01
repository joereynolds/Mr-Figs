import src.entity as entity
import src.static_scenes
import src.colours as colours

class Torch(entity.Entity):
    def __init__(self, x, y, width, height, image=None):
        entity.Entity.__init__(self, x, y, width, height, image)
