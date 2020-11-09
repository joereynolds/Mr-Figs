"""
Renders out a display of the count of bombs left on a player
"""
import pygame

from src.gui.text_element import TextElement
from src.entity import Entity
from src.actor import Actor
import src.colours as colours
import src.config as config

class BombDisplay(Entity):

    def __init__(self, x: int, y: int, width: int, height: int, surface, image=None):
        Entity.__init__(self, x, y, width, height, image)
        self.image.fill(colours.RED_GLOW)
        self.image.set_alpha(50)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surface = surface
        self.text = TextElement(text = 'BOMBS: ' )

    def render(self, bomb_count):
        """Renders text at the default position of (0,0) or otherwise
        if a position is supplied.
        @position = Position for the text to be rendered (optional)
        """
        font_object = pygame.font.Font(None, 20)
        rendered_text = font_object.render(self.text.text + str(bomb_count), False, colours.BLACK)
        self.surface.blit(rendered_text, (self.x, self.y))
