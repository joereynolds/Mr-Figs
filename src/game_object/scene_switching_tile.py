import src.entity as entity
import src.environment
import src.colours as colours

class SceneSwitchingTile(entity.Entity):
    def __init__(self, x, y, width, height, scene, image=None):
        entity.Entity.__init__(self, x, y, width, height, image)
        self.minimap_colour = colours.WHITE
        self.scene = scene

    def handle_collision(self, tile, player, level):
        if player.destination[0] == self.rect.x and player.destination[1] == self.rect.y:
            level.switch_to_scene(self.scene);

    def handle_pre_bomb_particle_creation(self, level):
        return False
