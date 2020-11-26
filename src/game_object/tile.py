import src.colours as colours
import src.entity as entity

class Tile(entity.Entity):
    """The tile class represents any tile in the game background,
        or foreground.
        It extends the entity class
        to add collision mechanics and various other bits"""

    def __init__(self, x, y, width, height, solid, destructable, image=None):
        entity.Entity.__init__(self, x, y, width, height, image)
        self.solid = bool(solid)
        self.destructable = destructable
        
        self.minimap_colour = colours.GREEN

        if self.solid:
            self.minimap_colour = colours.GREEN_BASE

        if self.destructable:
            self.minimap_colour = colours.BROWN_HIGHLIGHT
