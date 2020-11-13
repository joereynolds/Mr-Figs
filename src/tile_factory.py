from src.game_object.tile import Triggerable
from src.game_object.tile import MoveableTile
from src.game_object.tile import FinishTile
from src.game_object.tile import Stateful
from src.game_object.tile import Tile
from src.game_object.bomb import Bomb
from src.game_object.actor import Actor
from src.game_object.pickup_bomb import PickupBomb

class TileFactory():

    def build(self, tile_type, **kwargs):
        tile_map = {
            'triggerable': Triggerable,
            'finish_tile': FinishTile,
            'moveable_tile': MoveableTile,

            # stateful and pressure_plate only differ by the sprites they have.
            # I thought this easier than making separate classes for both, we'll see.
            'stateful': Stateful,
            'pressure_plate': Stateful,
            'bomb': Bomb,
            'actor': Actor,
            'tile': Tile,
            'pickup_bomb': PickupBomb
        }

        return tile_map[tile_type](**kwargs)
