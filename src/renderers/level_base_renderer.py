import pygame
import os
from src.gui.minimap import Minimap
from src.gui.data_display import DataDisplay
from src.game_object.light_source import LightSource
from src.game_object.finish_tile import FinishTile
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

        self.game_area = self.level.surface.subsurface(
            pygame.Rect(
                0,
                64,
                self.width,
                self.height - 64
            )
        )

        self.top_bar = self.level.surface.subsurface(
            pygame.Rect(
                0,
                0,
                self.width,
                64
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

        file_without_extension = os.path.splitext(self.level.file)[0]
        fallback_level_name = str.replace(file_without_extension, '-', ' ')
        level_name = self.level.tiled_level.properties.get('display_name', fallback_level_name)

        self.level_name_display = DataDisplay(
            self.width // 2,
            self.top_bar.get_height() // 2,
            quarter_of_screen,
            self.height,
            self.top_bar,
            os.path.basename(level_name)
        )

        self.veil = pygame.Surface((width - quarter_of_screen, height), flags=pygame.SRCALPHA)

        # Index all of our lightable sprites so we can references them straight away
        self.light_sources = []

        for sprite in self.level.sprites:
            # if isinstance(sprite, (Bomb, FinishTile, Triggerable)):
            if isinstance(sprite, (LightSource)):
                self.light_sources.append(sprite)

    def render_lights(self):
        self.veil.fill((50,50,50,155))
        ##offset = self.level.tiled_level.map_layer_for_camera.get_center_offset()

        translated = self.level.tiled_level.map_layer_for_camera.translate_rect(self.level.player.rect)

        # self.level.player.light_mask_rect = self.level.player.rect
        self.veil.blit(self.level.player.light_mask, 
            (
                translated.topleft
                # self.level.player.rect.x + 33,
                # self.level.player.rect.y + 64
            )
        )

        ##To debug, remove the special_flags arg
        ## needs blend_mult flag to work

        self.game_area.blit(self.veil, (0,0), special_flags=pygame.BLEND_MULT)
        # self.level.player.light_mask_rect.center = self.level.player.rect.center

    def render(self):
        if len(self.level.player.bombs) != self.bomb_count:
            pass
            #TODO shake the screen here
        else: self.level.surface.fill(self.colour)

        self.top_bar.fill((255,0,0))
        self.level.sprites.center(self.level.player.rect.center)
        self.level.sprites.draw(self.game_area)
        self.render_lights()

        self.minimap.render()
        self.bomb_display.render(self.level.player.remaining_bombs)

        self.game_area.blit(self.minimap.surface, (self.width - 200, 32))
        self.game_area.blit(self.bomb_display.surface, (self.width - 200, 200))
        self.level_name_display.render()


