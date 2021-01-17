from src.movement_vector import vector
import src.graphics as graphics
import src.entity as entity
import src.colours


from src.game_object.triggerable import Triggerable
from src.game_object.door import Door
from src.game_object.solid_tile import SolidTile
from src.game_object.scene_switching_tile import SceneSwitchingTile
from src.game_object.bomb import Bomb
from src.game_object.portal import Portal

class MoveableTile(SolidTile):
    def __init__(self, x, y, width, height, image=None):
        SolidTile.__init__(self, x, y, width, height, image)
        self.minimap_colour = src.colours.BROWN_BASE

        # A moveable tile cannot be pushed into any of these
        self.disallowed_tiles = (SolidTile, Bomb, SceneSwitchingTile)

    def handle_collision(self, tile, player, level):
        if player.destination[0] == self.rect.x and player.destination[1] == self.rect.y:
            target_x = self.rect.x + (vector[player.direction][0] * graphics.tile_width)
            target_y = self.rect.y + (vector[player.direction][1] * graphics.tile_width)

            target_tiles = level.tiled_level.get_tile_from_object_layer(target_x, target_y)

            for target_tile in target_tiles:
                # Don't go through lasers if they're on
                # TODO - This should rely on the state attribute instead of solid
                if isinstance(target_tile, Triggerable) and target_tile.solid:
                    return

                # Don't go through doors if they're closed 
                if isinstance(target_tile, Door) and not target_tile.open:
                    return

                if isinstance(target_tile, self.disallowed_tiles):
                    return

                if isinstance(target_tile, Portal):
                    # TODO - there exists a bug here. Basically we need to do what
                    # we're doing below and update the data
                    self.rect.x = target_tile.destination_portal.rect.x
                    self.rect.y = target_tile.destination_portal.rect.y
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

    def handle_pre_bomb_particle_creation(self, level):
        return False
