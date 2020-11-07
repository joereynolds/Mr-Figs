import random
import src.minimap as minimap
import src.colours as colours
import src.config as config

class LevelBaseRenderer():

    def __init__(self, level):
        self.level = level
        self.colour = random.choice(colours.BASE_COLOURS)
        self.bomb_count = len(self.level.player.bombs)

        self.minimap = minimap.Minimap(
                config.screen_width - (minimap.Minimap.WIDTH + 5), 
                5, 
                minimap.Minimap.WIDTH, 
                minimap.Minimap.HEIGHT, level
        )
        self.level.sprites.add(self.minimap)

    def render(self):
        if len(self.level.player.bombs) != self.bomb_count:
            pass
            #TODO shake the screen here
        else: self.level.surface.fill(self.colour)

        self.minimap.map.draw(self.level.surface)
        self.level.sprites.draw(self.level.surface)
