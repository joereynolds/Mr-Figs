#TODO Call this file scenes and place in the
#scenes directory?
import os
import config
import scenes.levelbase as level_base
import scenes.startmenu as start_menu
import scenes.levelselect as level_select
import scenes.escapemenu_no_overlay as escape_menu

def create_level_list():
    """Returns an array of LevelBase's, each one
    created from a level in our levels directory"""
    levels = os.listdir(config.level_location)
    levels.sort()

    level_dict = {}
    for index, level in enumerate(levels):
        key_name = 'level-' + str(index)
        level_dict[key_name] = level_base.LevelBase(config.level_location + level, 'NoNextScene')

    level_dict['start-menu'] = start_menu.StartMenu()
    level_dict['escape-menu'] = escape_menu.EscapeMenuNoOverlay()
    level_dict['level-select'] = level_select.LevelMenu(level_dict)

    return level_dict

def link_levels(level_list):
    """Sets the next level for each level so that when
    we finish that level it automatically takes us to
    the next one specified"""
    level_list['level-0'].next_level = level_list['level-1']
    level_list['level-1'].next_level = level_list['level-2']
    level_list['level-2'].next_level = level_list['level-3']

level_obj_list = create_level_list()
#TODO this works on reference, gross.
link_levels(level_obj_list)
