"""
This module contains a mock player. It is
the mock players job to play the game
over and over discovering any bugs. The mock player
follows a series of predefined movements by me
"""
from game import Game
import pygame
import environment

scenes = {
    'start-menu' : environment.level_obj_list[0],
    'level-1' : environment.level_obj_list[1]
} 

#need to look into this
mocker = Game(60)
mocker.run_mock(scenes['start-menu'])
scenes['start-menu'].switch_to_scene(scenes['level-1'])
