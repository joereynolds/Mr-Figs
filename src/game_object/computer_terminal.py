import src.entity as entity
import src.static_scenes
import src.colours as colours

class ComputerTerminal(entity.Entity):
    def __init__(self, x, y, width, height, minigame, image=None):
        entity.Entity.__init__(self, x, y, width, height, image)
        self.minimap_colour = colours.WHITE
        self.minigame = minigame

    def handle_collision(self, tile, player, level):
        if player.destination[0] == self.rect.x and player.destination[1] == self.rect.y:
            self.image.fill((255,0,0))
            level.switch_to_scene(self.minigame, minigame=True);

    def handle_pre_bomb_particle_creation(self, level):
        return False
