"""
There's a class per level.'
@KEY_NAME    = The name of the level for the level_dict in environment.py
               (This is only here for legacy reasons, remove when we can)
@NAME        = The filename of the level generated from Tiled
@LOCATION    = The full path to the level data
@IS_COMPLETE = Whether the level has been completed or not
"""
import config


class level1(object):
    KEY_NAME = 'level-1'
    NAME = 'new-level1.tmx'
    LOCATION = config.level_location + NAME
    IS_COMPLETE = False

class level2(object):
    KEY_NAME = 'level-2'
    NAME = 'new-level2.tmx'
    LOCATION = config.level_location + NAME
    IS_COMPLETE = False

class level3(object):
    KEY_NAME = 'level-3'
    NAME = 'new-level3.tmx'
    LOCATION = config.level_location + NAME
    IS_COMPLETE = False

class level4(object):
    KEY_NAME = 'level-4'
    NAME = 'new-level4.tmx'
    LOCATION = config.level_location + NAME
    IS_COMPLETE = False
