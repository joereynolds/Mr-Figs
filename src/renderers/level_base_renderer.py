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

        self.game_area = self.level.surface.subsurface(
            pygame.Rect(
                0,
                0,
                config.screen_width - 300,
                config.screen_height
            )
        )

        self.sidebar = self.level.surface.subsurface(
            pygame.Rect(
                config.screen_width - 300,
                0,
                300,
                config.screen_height
            )
        )

        self.minimap = Minimap(
            0,
            25,
            Minimap.WIDTH,
            Minimap.HEIGHT,
            level,
            self.sidebar
        )

        self.bomb_display = DataDisplay(
            0,
            200,
            Minimap.WIDTH,
            Minimap.HEIGHT,
            self.sidebar,
            'BOMBS '
        )

        self.turn_display = DataDisplay(
            0,
            225,
            Minimap.WIDTH,
            Minimap.HEIGHT,
            self.sidebar,
            'TURNS  TAKEN '
        )

        self.ace_turn_display = DataDisplay(
            0,
            250,
            Minimap.WIDTH,
            Minimap.HEIGHT,
            self.sidebar,
            'TURNS  TO  ACE  '
        )

        file_without_extension = os.path.splitext(self.level.file)[0]
        pretty_level_name = str.replace(file_without_extension, '-', ' ')

        self.level_name_display = DataDisplay(
            0,
            0,
            Minimap.WIDTH,
            Minimap.HEIGHT,
            self.sidebar,
            os.path.basename(pretty_level_name)
        )

    def render(self):
        if len(self.level.player.bombs) != self.bomb_count:
            pass
            #TODO shake the screen here
        else: self.level.surface.fill(self.colour)

        self.level.sprites.center(self.level.player.rect.center)
        self.level.sprites.draw(self.game_area)

        self.sidebar.fill(colours.BLUE_BASE)
        self.minimap.render()
        self.bomb_display.render(self.level.player.remaining_bombs)
        self.turn_display.render(self.level.player.turns_taken)
        self.ace_turn_display.render(self.level.tiled_level.properties.get('turns_to_ace', 'TODO'))
        self.level_name_display.render()
