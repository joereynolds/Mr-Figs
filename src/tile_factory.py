from src.game_object.triggerable import Triggerable
from src.game_object.barrel import Barrel
from src.game_object.scene_switching_tile import SceneSwitchingTile
from src.game_object.torch import Torch
from src.game_object.door import Door
from src.game_object.moveable_tile import MoveableTile
from src.game_object.destructible_tile import Destructible
from src.game_object.switch_tile import Switch
from src.game_object.portal import Portal
from src.game_object.pressure_plate import PressurePlate
from src.game_object.solid_tile import SolidTile
from src.game_object.bomb import Bomb
from src.game_object.actor import Actor
from src.game_object.pickup_bomb import PickupBomb
from src.game_object.video_tape import VideoTape
from src.game_object.path import Path
from src.game_object.platform import Platform
from src.game_object.enemy_pathable import EnemyPathable
from src.game_object.enemy_bombable import EnemyBombable
from src.game_object.particle_emitter import ParticleEmitter
from src.game_object.moving_platform import MovingPlatform
from src.game_object.moving_laser import MovingLaser
from src.game_object.computer_terminal import ComputerTerminal
from src.game_object.deadly_area import DeadlyArea

from src.minigames.hunt.player import Player
from src.minigames.hunt.collectible import Collectible

from src.minigames.lines.player import Player as LinesPlayer
from src.minigames.lines.collectible import Collectible as LinesCollectible


class TileFactory():

    def build(self, tile_type, **kwargs):
        # TODO automatically infer the class to create
        # We can split on '_' and TitleCase it and try
        # and create it
        # i.e.  some_other_tile: SomeOtherTile
        tile_map = {
            'triggerable': Triggerable,
            'moveable_tile': MoveableTile,
            'switch': Switch,
            'pressure_plate': PressurePlate,
            'bomb': Bomb,
            'actor': Actor,
            'tile': SolidTile,
            'pickup_bomb': PickupBomb,
            'portal': Portal,
            'video_tape': VideoTape,
            'destructible': Destructible,
            'path': Path,
            'platform': Platform,
            'moving_platform': MovingPlatform,
            'enemy_pathable': EnemyPathable,
            'enemy_bombable': EnemyBombable,
            'torch': Torch,
            'scene_switching_tile': SceneSwitchingTile,
            'barrel': Barrel,
            'barrel_left': Barrel,
            'barrel_right': Barrel,
            'barrel_up': Barrel,
            'barrel_up_left': Barrel,
            'barrel_up_right': Barrel,
            'barrel_down': Barrel,
            'barrel_down_left': Barrel,
            'barrel_down_right': Barrel,
            'particle_emitter': ParticleEmitter,
            'laser_up': MovingLaser,
            'laser_right': MovingLaser,
            'computer_terminal': ComputerTerminal,
            'door': Door,

            # Hunt minigame
            'minigame-hunt-player': Player,
            'minigame-hunt-collectible': Collectible,
            'deadly_area': DeadlyArea,

            # lines minigame
            'minigame_lines_player': LinesPlayer,
            'minigame_lines_collectible': LinesCollectible,
        }

        return tile_map[tile_type](**kwargs)
