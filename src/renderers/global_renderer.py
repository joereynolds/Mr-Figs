import pygame

class GlobalRenderer():
    """Global renderer is a wrapper around the other
    renderers. Not only that, it also means we are filling our surface,
    and flipping our displays less often"""

    def __init__(self, level):
        self.level = level

    def render(self):
        self.level.renderer.render()
        pygame.display.flip()
