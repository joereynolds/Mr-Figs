import os
import scenes.scenebase as scene_base
import scenes.levelbase as level_base
import scenes.startmenu as start_menu
import scenes.levelselect as level_select

# Automatically create an array of levelobjects that are
# linked to the next level. This enables us to just drop
# a file into our directory and it will load perfectly
# ..
levels_dir = '../levels/tmx/'
levels = os.listdir('../levels/tmx/')
level_obj_list = [level_base.LevelBase(levels_dir + level,'NoNextScene') for level in levels]

level_obj_list.insert(0, start_menu.StartMenu())
level_obj_list.insert(1, level_select.LevelMenu())
for i in range(len(level_obj_list)):
    if i == len(level_obj_list)-1:
        level_obj_list[i].next_level = level_obj_list[0]
    else:
        level_obj_list[i].next_level = level_obj_list[i+1]

