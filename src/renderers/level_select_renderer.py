import pygame
from src.gui.top_bar import TopBar
from src.game_object.torch import Torch
from src.scenes.escape_menu import EscapeMenu
import src.colours as colours
import src.config as config
import src.graphics as graphics

class LevelSelectRenderer():

    def __init__(self, level):
        self.level = level
        self.colour = colours.WHITE
        self.width, self.height = pygame.display.get_window_size()

        self.escape_menu = EscapeMenu()

        self.top_bar = TopBar(
            self.width, 
            graphics.tile_height * 4,
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

        for scene_switching_tile in self.level.scene_switching_tiles:
            # If we've completed the level, for now indicate it with
            # a green overlay
            if self.level.game_saver.has_completed_level(
                scene_switching_tile.scene
                ):
                veil = pygame.Surface((graphics.tile_width, graphics.tile_height)).convert_alpha()
                veil.fill((0,255,0, 125))
                scene_switching_tile.image.blit(veil, (0, 0))

    def render(self):
        self.level.surface.fill(self.colour)
        self.level.sprites.center(self.level.player.rect.center)
        self.level.sprites.draw(self.game_area)

        self.top_bar.render(self.level.surface)

        if self.escape_menu.is_visible:
            self.escape_menu.render(self.game_area)
