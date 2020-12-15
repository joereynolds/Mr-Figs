import pygame
import random
import os
from src.gui.data_display import DataDisplay
from src.gui.player_information_display import PlayerInformationDisplay
from src.gui.top_bar import TopBar
from src.game_object.light_source import LightSource
from src.game_object.torch import Torch
from src.game_object.triggerable import Triggerable
from src.game_object.bomb import Bomb
import src.colours as colours
import src.config as config
import src.graphics as graphics
from src.entity import Entity

class LevelBaseRenderer():

    def __init__(self, level):
        self.level = level
        self.colour = colours.WHITE
        self.bomb_count = len(self.level.player.bombs)
        self.width, self.height = pygame.display.get_window_size()

        self.top_bar = TopBar(self.width, 64, self.level)
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

        self.veil = pygame.Surface((self.width, self.height))

        self.light_sources = []

        for light_source in self.level.sprites:
            if isinstance(light_source, (Torch, Triggerable)):
                self.light_sources.append(light_source)

    def render_lights(self):
        self.veil.fill((50,50,50))
        self.veil.blit(
            self.level.player.light_mask.image, 
            (
                self.level.player.light_mask.rect.x,
                self.level.player.light_mask.rect.y,
            )
        )

        ## TODO - heavy stuff hsppening here, do it on __init__ to reduce the load Frodo.
        for light_source in self.light_sources:
            translated = self.level.tiled_level.map_layer_for_camera.translate_rect(light_source.rect)

            self.veil.blit(
                light_source.light_mask.image, 
                (
                    translated.x - graphics.tile_width * graphics.ZOOM_LEVEL,
                     # hardcoded to avoid calculations, source is light_source.light_mask.image.get_height() //2
                    translated.y - 128
                )
            )

        self.game_area.blit(self.veil, (0,0), special_flags=pygame.BLEND_MULT)

    def render(self):
        if len(self.level.player.bombs) != self.bomb_count:
            pass
            #TODO shake the screen here
        else: self.level.surface.fill(self.colour)

        self.level.sprites.center(self.level.player.rect.center)
        self.level.sprites.draw(self.game_area)
        self.render_lights()

        self.top_bar.render(self.level.surface)
        self.player_information_display.render(self.game_area)
