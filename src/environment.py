import os
import config
import scenes.levelbase as level_base
import scenes.startmenu as start_menu
import scenes.levelselect as level_select

def create_level_list():
    """Returns an array of LevelBase's, each one
    created from a level in our levels directory"""
    levels = os.listdir(config.level_location)
    levels.sort()

    level_list = [
        level_base.LevelBase(config.level_location + level, 'NoNextScene')
        for level in levels
    ]
    link_levels(level_list)
    return level_list

def link_levels(level_list):
    """Links all of ours levels to one another
    i.e. when you finish a level, it knows to go
    to the next one

    We make sure that if we're on the final level, then we link
    back to the first level.

    Otherwise, just link to the next level in the list"""
    for i in range(len(level_list)):
        #Loop back to the first item in the menu if we're at the end
        if i == len(level_list)-1:
            level_list[i].next_level = level_list[0]
        else:
            level_list[i].next_level = level_list[i+1]

#Create our default level list and forcibly add our
#level select menu and start menu to it.
level_obj_list = create_level_list()
level_obj_list.insert(0, start_menu.StartMenu())
level_obj_list.insert(1, level_select.LevelMenu())
link_levels(level_obj_list)
print(level_obj_list)
