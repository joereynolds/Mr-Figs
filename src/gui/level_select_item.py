"""
This is the card that displays on the level select menu for
each level.
"""
import pygame
import pytmx
import src.config as config
import src.colours as colours

from src.gui.clickable import Clickable

class LevelSelectItem(Clickable):

    def __init__(self, x: int, y: int, width: int, height: int, level_name: str, level_number: str, image = './data/placeholder-card-image.png'):
        map = pytmx.TiledMap(config.level_location + level_name)
        level_name = map.properties.get('display_name', level_name + 'NEED A NAME')

        Clickable.__init__(self, x, y, width, height, level_name)

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.level_number = str(level_number)

        self.shaded_area = pygame.Surface(
            (self.image.get_width(), self.image.get_height()),
            flags=pygame.SRCALPHA
        )

    def render(self):
        font_object = pygame.font.Font(None, self.font_size)
        rendered_text = font_object.render('[' + self.level_number + ']', False, colours.WHITE)
        self.image.blit(rendered_text, (5, self.height - 25))
        self.render_text(color=colours.WHITE)
