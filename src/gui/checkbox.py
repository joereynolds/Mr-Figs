import pygame
from src.gui.clickable import Clickable
    
class Checkbox(Clickable):

    def __init__(self, x, y, width, height, state):
        Clickable.__init__(self, x, y, width, height, '')
        self.state = 0

    def toggle(self):
        self.state = not self.state
