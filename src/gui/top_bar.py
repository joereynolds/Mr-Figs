import pygame
import os
from src.gui.data_display import DataDisplay


class TopBar():

    def __init__(self, width, height, level):
        self.width = width
        self.height = height

        file_without_extension = os.path.splitext(level.file)[0]
        fallback_level_name = str.replace(file_without_extension, '-', ' ')
        level_name = level.tiled_level.properties.get('display_name', fallback_level_name)

        self.surface = level.surface.subsurface(
            pygame.Rect(
                0,
                0,
                self.width,
                self.height
            )
        )

        self.level_name_display = DataDisplay(
            self.width // 2,
            self.height // 2,
            self.width,
            self.height,
            self.surface,
            os.path.basename(level_name)
        )

    def render(self, game_surface):
        self.surface.fill((255, 0, 0))
        self.level_name_display.render()
