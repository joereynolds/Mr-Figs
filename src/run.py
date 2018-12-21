#!/usr/bin/env python3

import game
import environment

if __name__ == '__main__':
    GAME = game.Game(60)
    GAME.run(environment.level_obj_list['start-menu'])

