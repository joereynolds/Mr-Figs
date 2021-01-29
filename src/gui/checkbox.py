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
        self.state = state
        self.name = name
        self.image = sprites[self.state]
        self.width = width
        self.height = height

        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def toggle(self, function, *args):
        self.state = not self.state

        self.image = sprites[self.state]
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        function(*args)

    def render(self):
        pass
