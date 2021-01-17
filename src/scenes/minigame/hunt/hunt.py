import pygame
import src.graphics as graphics
import src.colours as colours
import src.config as config
import src.scenes.scenebase as scene_base
from src.scenes.minigame.hunt.input_handler import InputHandler
from src.gui.clickable import Clickable
from src.resolution_asset_sizer import ResolutionAssetSizer
from src.game_object.minigame.hunt.player import Player
from src.game_object.minigame.hunt.collectible import Collectible
from src.tiled_map import TiledMap

class Hunt(scene_base.SceneBase):
    """The Hunt minigame...pretty much snake"""

    def __init__(self, file, previous, current_stage=1):
        self.current_stage = current_stage
        self.file = './data/levels/tmx/minigame-hunt-' + str(self.current_stage) + '.tmx'
        self.surface = graphics.get_window_surface()
        self.tiled_map = TiledMap(self.file, self.surface)
        self.sprites = self.tiled_map.sprites
        self.player = self.get_player()

        scene_base.SceneBase.__init__(
            self, 
            InputHandler(self),
            graphics.get_controller()
        ) 

        self.previous = previous
        self.width, self.height = pygame.display.get_window_size()

    def update(self, delta_time):
        self.sprites.update(delta_time, self.tiled_map)

        for sprite in self.sprites:
            if hasattr(sprite, 'handle_collision'):
                sprite.handle_collision(self.player)

        if not self.player.alive():
            self.reset()

        if self.has_completed_minigame():
            self.switch_to_scene(self.previous)
        elif self.has_won():
            self.next_stage()


    def has_won(self):
        has_no_enemies = True
        for sprite in self.sprites:
            if isinstance(sprite, Collectible):
                has_no_enemies = False

        return has_no_enemies

    def has_completed_minigame(self):
        return self.has_won() and self.current_stage == 3

    def render(self):
        self.surface.fill(colours.RED)
        self.sprites.draw(self.surface)

    def get_player(self):
        for sprite in self.sprites:
            if isinstance(sprite, Player):
                return sprite

    def reset(self):
        self.__init__(self.file, self.previous, self.current_stage)

    def next_stage(self):
        self.current_stage += 1
        self.__init__(self.file, self.previous, self.current_stage)
