import pygame
import src.graphics as graphics
import src.colours as colours
import src.config as config
import src.scenes.scenebase as scene_base
from src.scenes.minigame.hunt.input_handler import InputHandler
from src.gui.clickable import Clickable
from src.resolution_asset_sizer import ResolutionAssetSizer
from src.game_object.minigame.hunt.player import Player
from src.tiled_map import TiledMap

class Hunt(scene_base.SceneBase):
    """The Hunt minigame....pretty much snake"""

    def __init__(self, file):
        self.file = file

        self.surface = graphics.get_window_surface()
        self.tiled_map = TiledMap(file, self.surface)
        self.sprites = self.tiled_map.sprites
        self.player = self.get_player()

        scene_base.SceneBase.__init__(
            self, 
            InputHandler(self),
            graphics.get_controller()
        ) 

        self.width, self.height = pygame.display.get_window_size()

    def update(self, delta_time):
        self.sprites.update(delta_time)

    def render(self):
        """Renders all the buttons on our escape menu"""
        self.surface.fill(colours.RED)
        self.sprites.draw(self.surface)

    def get_player(self):
        for sprite in self.sprites:
            if isinstance(sprite, Player):
                return sprite
