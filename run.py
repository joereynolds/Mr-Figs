#!/usr/bin/env python3

import faulthandler

import src.game as game
import src.environment as environment

# Run program with
# python3 -Xfaulthandler run.py
# for better stacktraces
faulthandler.enable()


if __name__ == '__main__':
    GAME = game.Game(60)
    GAME.run(environment.level_obj_list['start-menu'])
