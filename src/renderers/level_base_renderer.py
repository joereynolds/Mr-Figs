import pygame
import os
from src.gui.minimap import Minimap
from src.gui.data_display import DataDisplay
import src.colours as colours
import src.config as config
import src.graphics as graphics
from src.entity import Entity
from src.effects import Fade

class LevelBaseRenderer():

    def __init__(self, level):
        self.level = level
        self.colour = colours.WHITE
        self.bomb_count = len(self.level.player.bombs)

        self.fade = Fade()
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

    def render(self):
        if len(self.level.player.bombs) != self.bomb_count:
            pass
            #TODO shake the screen here
        # else: self.level.surface.fill(self.colour)

        self.level.sprites.center(self.level.player.rect.center)
        self.level.sprites.draw(self.game_area)


        if self.level.player.has_finished_level:
            DURATION = 250
            start_time = pygame.time.get_ticks()
            ratio = 0.0 # alpha as a float [0.0 .. 1.0]
            while ratio < 1.0:
                current_time = pygame.time.get_ticks()
                elapsed = current_time - start_time
                ratio = elapsed / DURATION

                if elapsed >= DURATION:
                    self.level.switch_to_scene(self.level.tiled_level.properties['next_level']);

                self.fade.update(0, ratio)
                self.level.surface.blit(self.fade.veil, (0,0))
                pygame.display.flip()


        self.sidebar.fill(colours.BLUE_BASE)
        self.minimap.render()
        self.bomb_display.render(self.level.player.remaining_bombs)
        self.turn_display.render(self.level.player.turns_taken)
        self.ace_turn_display.render(self.level.tiled_level.properties.get('turns_to_ace', 'TODO'))
        self.level_name_display.render()
