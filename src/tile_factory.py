from src.game_object.triggerable import Triggerable
from src.game_object.moveable_tile import MoveableTile
from src.game_object.finish_tile import FinishTile
from src.game_object.destructible_tile import Destructible
from src.game_object.switch_tile import Switch
from src.game_object.portal import Portal
from src.game_object.pressure_plate import PressurePlate
from src.game_object.solid_tile import SolidTile
from src.game_object.bomb import Bomb
from src.game_object.actor import Actor
from src.game_object.pickup_bomb import PickupBomb
from src.game_object.video_tape import VideoTape

class TileFactory():

    def build(self, tile_type, **kwargs):
        tile_map = {
            'triggerable': Triggerable,
            'finish_tile': FinishTile,
            'moveable_tile': MoveableTile,
            'switch': Switch,
            'pressure_plate': PressurePlate,
            'bomb': Bomb,
            'actor': Actor,
            'tile': SolidTile,
            'pickup_bomb': PickupBomb,
            'portal': Portal,
            'video_tape': VideoTape,
            'destructible': Destructible
        }

        return tile_map[tile_type](**kwargs)
