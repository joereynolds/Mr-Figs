#!/usr/bin/env python3

import src.game as game
import src.environment as environment

if __name__ == '__main__':
    GAME = game.Game(60)
    GAME.run(environment.level_obj_list['start-menu'])
