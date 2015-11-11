
class LevelBaseRenderer():

    def __init__(self, level_base):

        self.level_base = level_base

    def render(self):
        self.level_base.surface.fill((255, 255, 255))
        self.level_base.sprites.draw(self.level_base.surface)

        if self.level_base.escape_menu.is_open:
            self.level_base.escape_menu.render()


