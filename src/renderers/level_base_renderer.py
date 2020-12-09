import pygame
import os
from src.gui.minimap import Minimap
from src.gui.data_display import DataDisplay
import src.colours as colours
import src.config as config
import src.graphics as graphics
from src.entity import Entity

class LevelBaseRenderer():

    def __init__(self, level):
        self.level = level
        self.colour = colours.WHITE
        self.bomb_count = len(self.level.player.bombs)
        print(self.level.file)

        width, height = pygame.display.get_window_size()
        quarter_of_screen = width // 4

        self.game_area = self.level.surface.subsurface(
            pygame.Rect(
                0,
                0,
                width,
                height
            )
        )

        self.minimap = Minimap(
            0,
            25,
            quarter_of_screen,
            height,
            level,
            self.game_area
        )

        self.bomb_display = DataDisplay(
            0,
            200,
            quarter_of_screen,
            height,
            self.game_area,
            'BOMBS '
        )

        file_without_extension = os.path.splitext(self.level.file)[0]
        fallback_level_name = str.replace(file_without_extension, '-', ' ')
        level_name = self.level.tiled_level.properties.get('display_name', fallback_level_name)

        self.level_name_display = DataDisplay(
            0,
            0,
            quarter_of_screen,
            height,
            self.game_area,
            os.path.basename(level_name)
        )

    def render(self):
        if len(self.level.player.bombs) != self.bomb_count:
            pass
            #TODO shake the screen here
        else: self.level.surface.fill(self.colour)

        self.level.sprites.center(self.level.player.rect.center)
        self.level.sprites.draw(self.game_area)

        self.minimap.render()
        self.bomb_display.render(self.level.player.remaining_bombs)
        self.level_name_display.render()
