import pygame
from src.gui.clickable import Clickable
import src.colours as colours
import src.graphics as g

sprites = {
    0: g.subsurf(g.grid(8,5)),
    1: g.subsurf(g.grid(7,5)),
}
    
class Checkbox(Clickable):

    def __init__(self, x, y, width, height, state, name):
        Clickable.__init__(self, x, y, width, height, string='')
        self.state = 0
        self.name = name

        self.toggle_colours = {
            0: colours.BLACK,
            1: colours.RED
        }

        self.image = sprites[self.state]
        self.image = pygame.transform.scale(self.image, (g.tile_width * 24, g.tile_height * 8))
        self.image = self.image.convert_alpha()

    def toggle(self, function, *args):
        self.state = not self.state
        function(*args)

    def render(self):
        self.image = sprites[self.state]
