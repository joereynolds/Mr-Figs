from src.scenes.levelselect import LevelSelect
from src.scenes.startmenu import StartMenu
from src.scenes.introduction_text_overlay import IntroductionTextOverlay
from src.scenes.credits import Credits
import src.config as config
from src.scenes.optionsmenu import OptionsMenu

def get_scenes():
    """
    Returns all scenes that need to be hardcoded.
    The majority of the levels are accessed via their filepath and
    so don't need to be in here. The only things that *should* be in here
    are menus and other scenes *not* present in the Tiled editor.
    """
    scenes = {}

    scenes['introduction'] = IntroductionTextOverlay()
    scenes['level-select'] = LevelSelect(config.level_location + 'L00-LevelSelect.tmx')
    scenes['start-menu'] = StartMenu()
    scenes['options-menu'] = OptionsMenu()
    scenes['credits'] = Credits()

    return scenes

level_obj_list = get_scenes()
