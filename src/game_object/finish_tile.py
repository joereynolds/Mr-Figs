from src.game_object.tile import Tile
import src.environment

class FinishTile(Tile):
    def __init__(self, x, y, width, height, solid, destructable, image=None):
        Tile.__init__(self, x, y, width, height, solid, destructable, image)

    def handle_collision(self, player, level):
        if player.destination[0] == self.rect.x and player.destination[1] == self.rect.y:
            level.switch_to_scene(src.environment.levels[level.file]['next_level'])
