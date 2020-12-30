import pygame
import random
import os
from src.scenes.text_overlay import TextOverlay
from src.gui.data_display import DataDisplay
from src.gui.player_information_display import PlayerInformationDisplay
from src.gui.top_bar import TopBar
from src.game_object.torch import Torch
from src.game_object.triggerable import Triggerable
from src.game_object.bomb import Bomb
from src.scenes.escape_menu import EscapeMenu
import src.colours as colours
import src.config as config
import src.graphics as graphics
from src.entity import Entity

class LevelRenderer():

    def __init__(self, level):
        self.level = level
        self.colour = colours.WHITE
        self.bomb_count = len(self.level.player.bombs)
        self.width, self.height = pygame.display.get_window_size()

        self.escape_menu = EscapeMenu()

        self.top_bar = TopBar(
            self.width, 
            graphics.tile_height * graphics.ZOOM_LEVEL, 
            self.level
        )

        self.player_information_display = PlayerInformationDisplay(
            self.width,
            self.height,
            self.level
        )

        self.game_area = self.level.surface.subsurface(
            pygame.Rect(
                0,
                self.top_bar.height,
                self.width,
                self.height - self.top_bar.height
            )
        )

        self.introduction_overlay = TextOverlay(
            """It is time.
            I have studied the Mad Professors schedule
            and can make my escape if I follow the path laid before me.
            I hear from 'The Others' that he's guilty of leaving evidence of these experiments just lying around.
            I should collect these and finally expose his wicked games!"
            """
        )

        self.intro_timer = 100

    def render(self):
        self.level.surface.fill(self.colour)
        self.level.sprites.center(self.level.player.rect.center)
        self.level.sprites.draw(self.game_area)

        self.top_bar.render(self.level.surface)
        self.player_information_display.render(self.game_area)

        if self.escape_menu.is_visible:
            self.escape_menu.render(self.game_area)

        # TODO - Gross - refactor this
        # If we're on the first level, show the intro screen
        if self.level.file == './data/levels/tmx/L01-Walking.tmx' and self.intro_timer > 0:
            self.introduction_overlay.render(self.level.surface)
            self.intro_timer -= 1
