#!/usr/bin/env python3

import faulthandler
import sys

import src.game as game
import src.static_scenes as scenes
from src.scenes.level import Level

# Run program with
# python3 -Xfaulthandler run.py
# for better stacktraces
# TODO
# Note this breaks windows (might just be because I have an older version on there though)
faulthandler.enable()

if __name__ == '__main__':
    GAME = game.Game(60)

    level = sys.argv[1] if len(sys.argv) > 1 else None

    if level:
        GAME.run(Level(level))
    else: GAME.run(scenes.level_obj_list['start-menu'])
