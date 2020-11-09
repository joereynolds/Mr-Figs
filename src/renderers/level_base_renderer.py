from src.minimap import Minimap
from src.bomb_display import BombDisplay
import src.colours as colours
import src.config as config

class LevelBaseRenderer():

    def __init__(self, level):
        self.level = level
        self.colour = colours.WHITE
        self.bomb_count = len(self.level.player.bombs)

        self.minimap = Minimap(
            config.screen_width - (Minimap.WIDTH + 5),
            5,
            Minimap.WIDTH,
            Minimap.HEIGHT,
            level,
            self.level.surface
        )

        self.bomb_display = BombDisplay(
            config.screen_width - (Minimap.WIDTH + 5),
            200,
            Minimap.WIDTH,
            Minimap.HEIGHT,
            self.level.surface,
        )
        self.level.sprites.add(self.minimap)

    def render(self):
        if len(self.level.player.bombs) != self.bomb_count:
            pass
            #TODO shake the screen here
        else: self.level.surface.fill(self.colour)

        self.minimap.render()
        self.bomb_display.render(self.level.player.remaining_bombs)
        self.level.sprites.draw(self.level.surface)
