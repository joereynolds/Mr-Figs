import pygame
import random
import os
from src.scenes.text_overlay import TextOverlay
from src.gui.minimap import Minimap
from src.gui.data_display import DataDisplay
from src.gui.player_information_display import PlayerInformationDisplay
from src.gui.top_bar import TopBar
from src.game_object.torch import Torch
from src.game_object.video_tape import VideoTape
from src.game_object.triggerable import Triggerable
from src.game_object.bomb import Bomb
from src.scenes.escape_menu import EscapeMenu
import src.colours as colours
import src.config as config
import src.graphics as graphics
from src.entity import Entity
from src.resolution_asset_sizer import ResolutionAssetSizer

class LevelRenderer():

    def __init__(self, level):
        self.level = level
        self.colour = colours.WHITE
        self.bomb_count = len(self.level.player.bombs)
        self.width, self.height = pygame.display.get_window_size()
        self.displaying_video_story = False
        asset_sizer = ResolutionAssetSizer()

        self.escape_menu = EscapeMenu()

        self.top_bar = TopBar(
            self.width, 
            asset_sizer.get_button_size((self.width, self.height))[1] * 0.75,
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

        self.game_area_rect = self.game_area.get_rect()

        self.minimap = Minimap(
            self.game_area_rect.centerx,
            self.game_area_rect.centery,
            self.width,
            self.height - self.top_bar.height,
            level
        )

    def render(self):
        self.level.surface.fill(self.colour)
        self.level.sprites.center(self.level.player.rect.center)
        self.level.sprites.draw(self.game_area)

        self.top_bar.render(self.level.surface)
        self.player_information_display.render(self.game_area)

        self.display_video_tape_story()

        if self.escape_menu.is_visible:
            self.escape_menu.render(self.game_area)

        if self.minimap.is_visible:
            self.minimap.render(self.game_area)

    def display_video_tape_story(self, video_tape: VideoTape = None):
        if video_tape is not None:
            video_tape.redirect_to=self.level
            self.level.switch_to_scene(
                "ignore me",
                video_tape_obj=video_tape
            )
