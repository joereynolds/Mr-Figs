#TODO Call this file scenes and place in the
#scenes directory?
import os
import src.config as config
from src.scenes.levelbase import LevelBase
import src.scenes.levelbase as level_base
import src.scenes.startmenu as start_menu
import src.scenes.game_over_menu as game_over_menu
import src.scenes.levelselect as level_select
import src.scenes.escapemenu_no_overlay as escape_menu


def create_level_list():
    """Returns an array of LevelBase's, each one
    created from a level in our levels directory"""
    level_dict = {}
    level_dir = './data/levels/tmx/'
    
    # TODO - This is bad. This creates all of our levels at once.
    # Might not be that bad? I think it's just memory (rather than CPU) hungry
    # investigate and find out at some point.
    for level in os.listdir(level_dir):
        level_dict[level] = LevelBase(level_dir + level, 'NoNextScene')

    level_dict['start-menu'] = start_menu.StartMenu()
    level_dict['game-over-menu'] = game_over_menu.GameOverMenu()
    level_dict['escape-menu'] = escape_menu.EscapeMenuNoOverlay()
    level_dict['level-select'] = level_select.LevelMenu(level_dict)

    return level_dict

def link_levels(level_list):
    """Sets the next level for each level so that when
    we finish that level it automatically takes us to
    the next one specified"""
    level_list['tutorial-movement.tmx'].next_level = level_list['tutorial-pushing.tmx']
    level_list['tutorial-pushing.tmx'].next_level = level_list['tutorial-bombing.tmx']
    level_list['tutorial-bombing.tmx'].next_level = level_list['1-level.tmx']
    level_list['1-level.tmx'].next_level = level_list['2-level.tmx']
    level_list['2-level.tmx'].next_level = level_list['3-level.tmx']
    level_list['3-level.tmx'].next_level = level_list['4-level.tmx']
    level_list['4-level.tmx'].next_level = level_list['1-level.tmx']

level_obj_list = create_level_list()
link_levels(level_obj_list)
