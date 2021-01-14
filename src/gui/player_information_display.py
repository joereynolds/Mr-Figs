from src.gui.minimap import Minimap
from src.gui.bomb_display import BombDisplay

class PlayerInformationDisplay():

    def __init__(self, width, height, level):
        self.width = width
        quarter_of_screen = self.width // 4
        self.height = height
        self.level = level

        self.bomb_display = BombDisplay(
            self.width - 200,
            200,
            quarter_of_screen,
            self.height
        )

    def render(self, game_surface):
        self.bomb_display.render(self.level.player.remaining_bombs)
        game_surface.blit(self.bomb_display.surface, (self.width - 200, 200))
