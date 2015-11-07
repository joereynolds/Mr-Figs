import os
import scenes.scenebase as scene_base
import scenes.levelbase as level_base
import scenes.startmenu as start_menu
import scenes.levelselect as level_select

def create_level_list():
    """Returns an array of LevelBase's, each one
    created from a level in our levels directory"""
    levels_dir = '../levels/tmx/'
    levels = os.listdir('../levels/tmx/')
    level_obj_list = [
        level_base.LevelBase(levels_dir + level,'NoNextScene')
        for level in levels
    ]
    for i in range(len(level_obj_list)):
        if i == len(level_obj_list)-1:
            level_obj_list[i].next_level = level_obj_list[0]
        else:
            level_obj_list[i].next_level = level_obj_list[i+1]
    return level_obj_list

#Create our default level list and forcibly add our
#level select menu and start menu to it.
level_obj_list = create_level_list()
level_obj_list.insert(0, start_menu.StartMenu())
level_obj_list.insert(1, level_select.LevelMenu())
for i in range(len(level_obj_list)):
    ##If it's the last level, put the 'next_level', as the start menu
    if i == len(level_obj_list)-1:
        level_obj_list[i].next_level = level_obj_list[0]
    else:
        level_obj_list[i].next_level = level_obj_list[i+1]
