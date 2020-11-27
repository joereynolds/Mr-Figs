from src.game_object.tile import Tile
from src.movement_vector import vector
import src.graphics as graphics

class MoveableTile(Tile):
    def __init__(self, x, y, width, height, solid, moveable=False, image=None):
        Tile.__init__(self, x, y, width, height, solid, image)

    def handle_collision(self, tile, player, level):
        if player.destination[0] == self.rect.x and player.destination[1] == self.rect.y:
            target_x = self.rect.x + (vector[player.direction][0] * graphics.tile_width)
            target_y = self.rect.y + (vector[player.direction][1] * graphics.tile_width)

            if level.tiled_level.find_solid_tile(
                level.tiled_level.get_tile_all_layers(target_x, target_y)
            ):
                return

            # Bit of an edge case that needs refactoring.  Basically a bug was
            # introduced (or never caught in the first place) where once you
            # pushed a moveable, bombs would pass through this was because we
            # need to update the object data within the tiled map itself
            # otherwise the tile itself has moved (which is fine) but it has
            # not updated in the data so when we go to grab something at that x
            # and y, it's not there.
            objects = level.tiled_level._map.get_layer_by_name('objects')
            for object in objects:
                if object.x == self.rect.x and object.y == self.rect.y:
                    object.x = target_x
                    object.y = target_y

            self.rect.x = target_x
            self.rect.y = target_y

