import src.entity as entity
import src.environment
import src.colours as colours
import pygame

class FinishTile(entity.Entity):
    def __init__(self, x, y, width, height, image=None):
        entity.Entity.__init__(self, x, y, width, height, image)
        self.minimap_colour = colours.WHITE

    def handle_collision(self, tile, player, level):
        if player.destination[0] == self.rect.x and player.destination[1] == self.rect.y:
            player.has_finished_level = True
            # level.switch_to_scene(level.tiled_level.properties['next_level']);

    def handle_pre_bomb_particle_creation(self, level):
        return False
