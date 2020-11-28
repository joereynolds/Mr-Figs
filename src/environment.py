import os
from src.scenes.levelbase import LevelBase
import src.scenes.levelbase as level_base
import src.scenes.startmenu as start_menu
import src.scenes.game_over_menu as game_over_menu
import src.scenes.levelselect as level_select
import src.scenes.escapemenu_no_overlay as escape_menu
import src.config as config
from src.scenes.optionsmenu import OptionsMenu

def create_level_list():
    """
    Returns all scenes that need to be hardcoded.
    The majority of the levels are accessed via their filepath and
    so don't need to be in here. The only things that *should* be in here
    are menus and other scenes *not* present in the Tiled editor.
    """
    level_dict = {}

    level_dict['tutorial-movement.tmx'] = LevelBase(config.level_location + 'L1-Walking.tmx')
    level_dict['start-menu'] = start_menu.StartMenu()
    level_dict['game-over-menu'] = game_over_menu.GameOverMenu()
    level_dict['escape-menu'] = escape_menu.EscapeMenuNoOverlay()
    level_dict['options-menu'] = OptionsMenu()
    level_dict['level-select'] = level_select.LevelMenu(level_dict)

    return level_dict

level_obj_list = create_level_list()
