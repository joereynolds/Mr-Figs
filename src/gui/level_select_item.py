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

    def __init__(self, x, y, width, height, level_name, level_number, image = './data/placeholder-card-image.png'):

        map = pytmx.TiledMap(config.level_location + level_name)

        level_name = map.properties.get('display_name', level_name + 'NEED A NAME')


        Clickable.__init__(self, x, y, width, height, level_name)

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))

        self.shaded_area = pygame.Surface(
            (self.image.get_width(), self.image.get_height()), 
            flags=pygame.SRCALPHA
        )

        self.shaded_area.fill((50, 50, 50, 0))
        self.image.blit(self.shaded_area, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)

        pygame.font.init()
        font_object = pygame.font.Font(None, 30)
        rendered_text = font_object.render('[' + str(level_number) + ']', False, colours.WHITE)
        self.image.blit(rendered_text, (5, height - 25))

        # self.rect = self.image.get_rect() 
        # self.rect.x = x
        # self.rect.y = y



