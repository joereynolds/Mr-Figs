#!/usr/bin/env python3

import faulthandler

import src.game as game
import src.static_scenes as scenes

# Run program with
# python3 -Xfaulthandler run.py
# for better stacktraces
# Note this breaks windows (might just be because I have an older version on there though)
faulthandler.enable()

if __name__ == '__main__':
    GAME = game.Game(60)
    GAME.run(scenes.level_obj_list['start-menu'])
