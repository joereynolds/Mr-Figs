import pygame
import os

class KeyboardController():

    NAME = 'keyboard'

    def get_name(self):
        return KeyboardController.NAME

    def get_down_button_state():
        return pygame.K_DOWN

    def get_up_button_state():
        return pygame.K_UP

    def get_action_button_image():
        base_path = os.path.join(
            'assets', 
            'images', 
            'controller-prompts',
            'keyboard-and-mouse', 
            'Light' + os.sep
        )

        return pygame.image.load(base_path + 'Space_Key_Light.png')

    def get_left_button_state():
        return pygame.K_LEFT

    def get_right_button_state():
        return pygame.K_RIGHT

    def get_select_button_state():
        return pygame.K_RETURN

    def get_action_button_state():
        return pygame.K_SPACE

    def get_secondary_button_state():
        return pygame.K_TAB

    def get_escape_button_state():
        return pygame.K_ESCAPE

    
