import main
import pygame
import environment

#start the game
mock_game = main.Game(60)
mock_game.run(environment.level_obj_list[0])

#click the start button
start_menu = environment.level_obj_list[0]
print('####################')
print(start_menu.component_dict)
