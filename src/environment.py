import os
from src.scenes.levelbase import LevelBase
import src.scenes.levelbase as level_base
import src.scenes.startmenu as start_menu
import src.scenes.game_over_menu as game_over_menu
import src.scenes.levelselect as level_select
import src.scenes.escapemenu_no_overlay as escape_menu


levels = {
    './data/levels/tmx/tutorial-movement.tmx': {
        'next_level': './data/levels/tmx/tutorial-pushing.tmx'
    },
    './data/levels/tmx/tutorial-pushing.tmx': {
        'next_level': './data/levels/tmx/tutorial-bombing.tmx'
    },
    './data/levels/tmx/tutorial-bombing.tmx': {
        'next_level': './data/levels/tmx/tutorial-picking-up-easy.tmx'
    },
    './data/levels/tmx/tutorial-picking-up-easy.tmx': {
        'next_level': './data/levels/tmx/tutorial-picking-up.tmx'
    },
    './data/levels/tmx/tutorial-picking-up.tmx': {
        'next_level': './data/levels/tmx/2-level.tmx'
    },
    './data/levels/tmx/2-level.tmx': {
        'next_level': './data/levels/tmx/5-level.tmx'
    },
    './data/levels/tmx/3-level.tmx': {
        'next_level': './data/levels/tmx/4-level.tmx'
    },
    './data/levels/tmx/4-level.tmx': {
        'next_level': './data/levels/tmx/5-level.tmx'
    },
    './data/levels/tmx/5-level.tmx': {
        'next_level': './data/levels/tmx/6-level.tmx'
    },
    './data/levels/tmx/6-level.tmx': {
        'next_level': './data/levels/tmx/lotta-lasers.tmx'
    },
}
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
