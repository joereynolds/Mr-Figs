import src.entity as entity
import src.colours as colours

class PickupBomb(entity.Entity):
    """The tile class represents any tile in the game background,
        or foreground.
        It extends the entity class
        to add collision mechanics and various other bits"""

    def __init__(self, x, y, width, height, image=None):
        entity.Entity.__init__(self, x, y, width, height, image)

        self.minimap_colour = colours.GREEN
