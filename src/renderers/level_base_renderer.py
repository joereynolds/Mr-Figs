import pygame
import os
from src.gui.minimap import Minimap
from src.gui.data_display import DataDisplay
from src.game_object.light_source import LightSource
import src.colours as colours
import src.config as config
import src.graphics as graphics
from src.entity import Entity

class LevelBaseRenderer():

    def __init__(self, level):
        self.level = level
        self.colour = colours.WHITE
        self.bomb_count = len(self.level.player.bombs)
        # self.fader = Fader(self.level)
        print(self.level.file)

        width, height = pygame.display.get_window_size()
        quarter_of_screen = width // 4

        self.game_area = self.level.surface.subsurface(
            pygame.Rect(
                0,
                0,
                width - quarter_of_screen,
                height
            )
        )

        self.sidebar = self.level.surface.subsurface(
            pygame.Rect(
                width - quarter_of_screen,
                0,
                quarter_of_screen,
                height
            )
        )

        self.minimap = Minimap(
            0,
            25,
            quarter_of_screen,
            height,
            level,
            self.sidebar
        )

        self.bomb_display = DataDisplay(
            0,
            200,
            quarter_of_screen,
            height,
            self.sidebar,
            'BOMBS '
        )

        self.turn_display = DataDisplay(
            0,
            225,
            quarter_of_screen,
            height,
            self.sidebar,
            'TURNS  TAKEN '
        )

        self.ace_turn_display = DataDisplay(
            0,
            250,
            quarter_of_screen,
            height,
            self.sidebar,
            'TURNS  TO  ACE  '
        )

        file_without_extension = os.path.splitext(self.level.file)[0]
        fallback_level_name = str.replace(file_without_extension, '-', ' ')
        level_name = self.level.tiled_level.properties.get('display_name', fallback_level_name)

        self.level_name_display = DataDisplay(
            0,
            0,
            quarter_of_screen,
            height,
            self.sidebar,
            os.path.basename(level_name)
        )

        self.veil = pygame.Surface((width, height), flags=pygame.SRCALPHA)
        self.light = pygame.image.load('./data/light-soft.png')


        # Index all of our lightable sprites so we can references them straight away
        # self.light_sources = []

        # for sprite in self.level.sprites:
        #     if isinstance(sprite, LightSource):
        #         self.light_sources.append(sprite)



    def render_lights(self):
        pass
        # self.veil.fill((50,50,50,155))

        # for light_source in self.level.sprites:
        #     if isinstance(light_source, LightSource):
        #         self.veil.blit(
        #             light_source.image, 
        #             light_source.rect
        #         )

        #To debug, remove the special_flags arg
        # needs blend_mult flag to work
        # self.game_area.blit(self.veil, (0,0), )

    def render(self):
        if len(self.level.player.bombs) != self.bomb_count:
            pass
            #TODO shake the screen here
        else: self.level.surface.fill(self.colour)

        self.level.sprites.center(self.level.player.rect.center)
        self.level.sprites.draw(self.game_area)
        self.render_lights()

        self.sidebar.fill(colours.BLUE_BASE)
        self.minimap.render()
        self.bomb_display.render(self.level.player.remaining_bombs)
        self.turn_display.render(self.level.player.turns_taken)
        self.ace_turn_display.render(self.level.tiled_level.properties.get('turns_to_ace', 'TODO'))
        self.level_name_display.render()


