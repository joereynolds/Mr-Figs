from src.tile import Triggerable
from src.tile import FinishTile
from src.tile import Stateful
from src.tile import Tile
from src.bomb import Bomb
from src.actor import Actor

class TileFactory():

    def build(self, tile_type, **kwargs):
        tile_map = {
            'triggerable': Triggerable,
            'finish_tile': FinishTile,
            'stateful': Stateful,
            'bomb': Bomb,
            'actor': Actor,
            'tile': Tile
        }

        return tile_map[tile_type](**kwargs)
