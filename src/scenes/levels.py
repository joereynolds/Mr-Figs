"""
There's a class per level.'
@KEY_NAME    = The name of the level for the level_dict in environment.py
               (This is only here for legacy reasons, remove when we can)
@NAME        = The filename of the level generated from Tiled
@LOCATION    = The full path to the level data
@IS_COMPLETE = Whether the level has been completed or not
"""
import src.config as config
import src.scenes.levelbase as level_base

class level5(object):
    KEY_NAME = 'level-4'
    NAME = '4-level.tmx'
    LOCATION = config.level_location + NAME
    IS_COMPLETE = False

class level4(object):
    KEY_NAME = 'level-3'
    NAME = '3-level.tmx'
    LOCATION = config.level_location + NAME
    IS_COMPLETE = False

class level3(object):
    KEY_NAME = 'level-2'
    NAME = '2-level.tmx'
    LOCATION = config.level_location + NAME
    IS_COMPLETE = False

class level2(object):
    KEY_NAME = 'level-1'
    NAME = '1-level.tmx'
    LOCATION = config.level_location + NAME
    IS_COMPLETE = False

class level1(object):
    KEY_NAME = 'level-0'
    NAME = '0-introduction.tmx'
    LOCATION = config.level_location + NAME
    IS_COMPLETE = False
    NEXT_LEVEL = (level2.LOCATION, 'NoNextScene')

