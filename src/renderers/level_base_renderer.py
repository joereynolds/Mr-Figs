import random
import src.colours as colours

class LevelBaseRenderer():

    def __init__(self, level):

        self.level = level
        self.colour = random.choice(colours.BASE_COLOURS)
        self.bomb_count = len(self.level.player.bombs)

    def render(self):

        if len(self.level.player.bombs) != self.bomb_count:
            pass
            #TODO shake the screen here
        else: self.level.surface.fill(self.colour)
    
        self.level.sprites.draw(self.level.surface)
