import os
from src.scenes.levelbase import LevelBase
import src.scenes.levelbase as level_base
import src.scenes.startmenu as start_menu
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

    level_dict['level-select'] = LevelBase(config.level_location + 'L00-LevelSelect.tmx')
    level_dict['start-menu'] = start_menu.StartMenu()
    level_dict['options-menu'] = OptionsMenu()

    return level_dict

level_obj_list = create_level_list()
