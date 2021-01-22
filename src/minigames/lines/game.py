import pygame
import src.graphics as graphics
import src.colours as colours
import src.config as config
import src.scenes.scenebase as scene_base
from src.minigames.lines.input_handler import InputHandler
from src.gui.clickable import Clickable
from src.resolution_asset_sizer import ResolutionAssetSizer
from src.minigames.lines.player import Player
from src.minigames.lines.collectible import Collectible
from src.tiled_map import TiledMap
from src.game_object.deadly_area import DeadlyArea

class Lines(scene_base.SceneBase):
    """The Lines minigame"""

    def __init__(self, previous, current_stage=1):
        self.current_stage = current_stage
        self.file = './assets/game-data/levels/minigames/lines/minigame_lines_' + str(self.current_stage) + '.tmx'
        self.surface = graphics.get_window_surface()
        self.tiled_map = TiledMap(self.file, self.surface)
        self.sprites = self.tiled_map.sprites
        self.player = self.get_player()
        self.collectibles = pygame.sprite.Group([sprite for sprite in self.sprites if isinstance(sprite, Collectible)])
        self.collideables = pygame.sprite.Group([sprite for sprite in self.sprites if isinstance(sprite, DeadlyArea)])

        scene_base.SceneBase.__init__(
            self, 
            InputHandler(self),
            graphics.get_controller()
        ) 

        self.previous = previous
        self.width, self.height = pygame.display.get_window_size()

    def update(self, delta_time):
        self.sprites.update(delta_time, self.tiled_map)
        self.player.handle_collision(self.collectibles, self.collideables)

        if not self.player.alive():
            self.reset()

        if self.has_completed_minigame():
            self.previous.open_secured_door()
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
                print(sprite)
                return sprite

    def reset(self):
        self.__init__(self.previous, self.current_stage)

    def next_stage(self):
        self.current_stage += 1
        self.__init__(self.previous, self.current_stage)
