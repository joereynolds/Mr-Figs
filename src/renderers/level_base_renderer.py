import random
import colours

class LevelBaseRenderer():

    def __init__(self, level_base):

        self.level_base = level_base
        self.colour = random.choice(colours.BASE_COLOURS)

    def render(self):
        self.level_base.surface.fill(self.colour)
        self.level_base.sprites.draw(self.level_base.surface)

        # if self.level_base.escape_menu.is_open:
        #     self.level_base.escape_menu.render()


