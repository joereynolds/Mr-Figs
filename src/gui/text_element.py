import pygame


class TextElement(pygame.font.Font):
    """Contains all methods and parameters for text.
    @text = The string of text you want to display
    @size = The size of the font
    @position = The position of the text relative to the surface
    @color = An rgb colour """

    def __init__(self, color=(255, 255, 255), text='Change me', size='12', position=(0, 0)):
        self.text = text
        self.size = size
        self.color = (color)
        self.position = position

    def set_color(self, color):
        self.color = color
