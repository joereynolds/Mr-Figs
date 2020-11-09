import src.entity as entity
import src.colours as colours
import src.graphics as graphics

class BombParticle(entity.Entity):
    """
    A graphical representation of the explosion surrounding the bomb
    """
    def __init__(self, x, y, width, height):
        image = graphics.sprites['explosion']['sprites'][0]
        entity.Entity.__init__(self, x, y, width, height, image)
        self.minimap_colour = colours.RED_GLOW


