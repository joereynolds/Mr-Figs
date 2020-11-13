from src.tile import Triggerable
from src.tile import MoveableTile
from src.tile import FinishTile
from src.tile import Stateful
from src.tile import Tile
from src.bomb import Bomb
from src.actor import Actor
from src.pickup_bomb import PickupBomb

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
