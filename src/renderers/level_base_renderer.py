import pygame
import os
from src.gui.minimap import Minimap
from src.gui.data_display import DataDisplay
from src.gui.top_bar import TopBar
from src.game_object.light_source import LightSource
from src.game_object.finish_tile import FinishTile
from src.game_object.torch import Torch
from src.game_object.triggerable import Triggerable
from src.game_object.bomb import Bomb
from src.gui.bomb_display import BombDisplay
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

        self.width, self.height = pygame.display.get_window_size()
        quarter_of_screen = self.width // 4

        self.top_bar = TopBar(self.width, 64, self.level)

        self.game_area = self.level.surface.subsurface(
            pygame.Rect(
                0,
                self.top_bar.height,
                self.width,
                self.height - self.top_bar.height
            )
        )

        self.minimap = Minimap(
            self.width - 200,
            32,
            quarter_of_screen,
            self.height,
            level
        )

        self.bomb_display = BombDisplay(
            self.width - 200,
            200,
            quarter_of_screen,
            self.height
        )

        self.veil = pygame.Surface((self.width, self.height), flags=pygame.SRCALPHA)

        self.light_sources = []

        for light_source in self.level.sprites:
            if isinstance(light_source, (Torch, Triggerable)):
                self.light_sources.append(light_source)


    def render_lights(self):
        self.veil.fill((50,50,50,155))
        # TODO - heavy stuff hsppening here, do it on __init__ to reduce the load Frodo.

        translated = self.level.tiled_level.map_layer_for_camera.translate_rect(self.level.player.rect)

        self.veil.blit(
            self.level.player.light_mask.image, 
            (
                translated.x - graphics.tile_width * graphics.ZOOM_LEVEL,
                # hardcoded to avoid calculations, the source is self.level.player.light_mask.image.get_height() //2
                translated.y - 128 
            )
        )

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


        ##To debug, remove the special_flags arg needs blend_mult flag to work
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
        self.minimap.render()
        self.bomb_display.render(self.level.player.remaining_bombs)

        self.game_area.blit(self.minimap.surface, (self.width - 200, 32))
        self.game_area.blit(self.bomb_display.surface, (self.width - 200, 200))
