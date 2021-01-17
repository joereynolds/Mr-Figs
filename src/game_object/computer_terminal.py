import src.entity as entity
import src.static_scenes
import src.colours as colours
import src.graphics as graphics

class ComputerTerminal(entity.Entity):
    def __init__(self, x, y, width, height, minigame, image=None):
        entity.Entity.__init__(self, x, y, width, height, image)
        self.minigame = minigame
        self.image = graphics.subsurf(graphics.grid(2, 10))
        self.broken_image = graphics.subsurf(graphics.grid(1, 10))

    def handle_collision(self, tile, player, level):
        if player.destination[0] == self.rect.x and player.destination[1] == self.rect.y:
            level.switch_to_scene(self.minigame, minigame=True);
            self.image = self.broken_image

    def handle_pre_bomb_particle_creation(self, level):
        return False
