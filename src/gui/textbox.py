import pygame
from typing import List

import src.config as config
from src.resolution_asset_sizer import ResolutionAssetSizer

class Textbox(pygame.sprite.Sprite):

    def __init__(
            self, 
            x: int, 
            y: int, 
            width: int, 
            height: int, 
            lines: List[str]
        ):
        pygame.sprite.Sprite.__init__(self)

        self.index = 0
        self.text = lines
        self.image = pygame.Surface((width, height)).convert_alpha()
        self.width = width
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.size = pygame.display.get_window_size()

        self.asset_sizer = ResolutionAssetSizer()
        self.font_size = self.asset_sizer.get_font_size(self.size, 8)

        pygame.font.init()
        self.font = pygame.font.Font(config.font, self.font_size)

    def increment(self):
        self.index += 1

    def render(self, surface):
        self.wrap_text(
            self.text[self.index], 
            self.font,
            (255, 255, 255),
            self.rect.x,
            self.rect.y,
            surface,
            self.width
        )

    def wrap_text(self, text: str, font, colour, x, y, surface, allowed_width):
        words = text.split()

        # now, construct lines out of these words
        lines = []
        while len(words) > 0:
            # get as many words as will fit within allowed_width
            line_words = []
            while len(words) > 0:
                line_words.append(words.pop(0))
                fw, fh = font.size(' '.join(line_words + words[:1]))
                if fw > allowed_width:
                    break

            # add a line consisting of those words
            line = ' '.join(line_words)
            lines.append(line)

        # now we've split our text into lines that fit into the width, actually
        # render them

        # we'll render each line below the last, so we need to keep track of
        # the culmative height of the lines we've rendered so far
        y_offset = 0
        for line in lines:
            fw, fh = font.size(line)
            ty = y + y_offset

            font_surface = font.render(line, True, colour)
            surface.blit(font_surface, (x, ty))

            y_offset += fh
