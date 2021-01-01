import pygame
import src.colours as colours
import src.config as config
import src.scenes.scenebase as scene_base
import src.input_handlers.escape_menu_input_handler as input_handler
from src.gui.clickable import Clickable

class TextOverlay(scene_base.SceneBase):
    """The menu that pops up during game when we press escape"""

    def __init__(self, text):
        # TODO needs its own input handler
        scene_base.SceneBase.__init__(self, input_handler.EscapeMenuInput(self)) 
        self.text = text

        self.is_visible = False
        self.width, self.height = pygame.display.get_window_size()
        self.center = self.width // 2
        self.surface = pygame.Surface((self.width, self.height)).convert()
        self.font_size = 24
        self.font = pygame.font.Font(config.font, self.font_size)

    def render(self, surface):
        """Renders all the buttons on our escape menu"""
        self.surface.fill(colours.BLACK)
        self.wrap_text(
            self.text, 
            self.font,
            colours.WHITE,
            self.center,
            100,
            self.surface, 
            self.center
        )

        surface.blit(self.surface, (0,0))

    def wrap_text(self, text: str, font, colour, x, y, screen, allowed_width):
        # first, split the text into words
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

            # (tx, ty) is the top-left of the font surface
            tx = x - fw / 2
            ty = y + y_offset

            font_surface = font.render(line, True, colour)
            screen.blit(font_surface, (tx, ty))

            y_offset += fh
