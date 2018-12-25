#TODO Call this file scenes and place in the
#scenes directory?
import os
import config
import scenes.levelbase as level_base
import scenes.levels as levels
import scenes.startmenu as start_menu
import scenes.game_over_menu as game_over_menu
import scenes.levelselect as level_select
import scenes.escapemenu_no_overlay as escape_menu

def create_level_list():
    """Returns an array of LevelBase's, each one
    created from a level in our levels directory"""
    level_dict = {}

    # TODO - This is very bad. This creates all of our levels at once.
    level_dict[levels.level1.KEY_NAME] = level_base.LevelBase(levels.level1.LOCATION, 'NoNextScene', 1)
    level_dict[levels.level2.KEY_NAME] = level_base.LevelBase(levels.level2.LOCATION, 'NoNextScene', 2)
    level_dict[levels.level3.KEY_NAME] = level_base.LevelBase(levels.level3.LOCATION, 'NoNextScene', 3)
    level_dict[levels.level4.KEY_NAME] = level_base.LevelBase(levels.level4.LOCATION, 'NoNextScene', 4)
    level_dict['start-menu'] = start_menu.StartMenu()
    level_dict['game-over-menu'] = game_over_menu.GameOverMenu()
    level_dict['escape-menu'] = escape_menu.EscapeMenuNoOverlay()
    level_dict['level-select'] = level_select.LevelMenu(level_dict)

    return level_dict

def link_levels(level_list):
    """Sets the next level for each level so that when
    we finish that level it automatically takes us to
    the next one specified"""
    level_list['level-1'].next_level = level_list['level-2']
    level_list['level-2'].next_level = level_list['level-3']

level_obj_list = create_level_list()
#TODO this works on reference, gross.
link_levels(level_obj_list)
