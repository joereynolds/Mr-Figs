import pygame
import math
import src.colours as colours

class Fade():
    """
    Fades out an element. This class should be passed 
    through to the component that requires fading

    Thanks to pyroller for implementation details:
    https://github.com/iminurnamez/pyroller/edit/master/data/components/flair_pieces.py
    """

    def __init__(self):
        self.faded = False
        self.veil = pygame.Surface(pygame.display.get_window_size()).convert()
        self.veil.fill(colours.BLACK)

    def update(self, delta_time, ratio):
        """
        Gradually increment the alpha value of the parent's
        surface.
        Once we're fully faded out, we're finished

        TODO - Consider delta time eventually
        """
        # TODO - this fades out nicely but I have no idea why
        self.veil.set_alpha(1)

