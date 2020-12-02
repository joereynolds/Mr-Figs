import pygame
from src.gui.clickable import Clickable
import src.colours as colours
    
class Checkbox(Clickable):

    def __init__(self, x, y, width, height, state):
        Clickable.__init__(self, x, y, width, height, '')
        self.state = 0

        self.toggle_colours = {
            0: colours.BLACK,
            1: colours.RED
        }

    def toggle(self, function, *args):
        self.state = not self.state
        function(*args)

    def render(self):
        self.image.fill(self.toggle_colours[self.state])

