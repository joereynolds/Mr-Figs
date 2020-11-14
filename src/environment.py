import os
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

    level_dict['tutorial-movement.tmx'] = LevelBase(level_dir + 'tutorial-movement.tmx')
    level_dict['start-menu'] = start_menu.StartMenu()
    level_dict['game-over-menu'] = game_over_menu.GameOverMenu()
    level_dict['escape-menu'] = escape_menu.EscapeMenuNoOverlay()
    level_dict['level-select'] = level_select.LevelMenu(level_dict)

    return level_dict

level_obj_list = create_level_list()
