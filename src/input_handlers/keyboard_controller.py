import pygame
import os
from src.user_data import UserData

class KeyboardController():

    NAME = 'keyboard'

    def __init__(self):
        user_data = UserData()
        self.config = user_data.get_controls()
        print(self.config)

    def get_name(self):
        return KeyboardController.NAME

    def get_down_button_state(self):
        return getattr(pygame, self.config['down'])

    def get_up_button_state(self):
        return getattr(pygame, self.config['up'])

    def get_action_button_image(self):
        base_path = os.path.join(
            'assets', 
            'images', 
            'controller-prompts',
            'keyboard-and-mouse', 
            'Light' + os.sep
        )

        return pygame.image.load(base_path + 'Space_Key_Light.png')

    def get_left_button_state(self):
        return getattr(pygame, self.config['left'])

    def get_right_button_state(self):
        return getattr(pygame, self.config['right'])

    def get_select_button_state(self):
        return getattr(pygame, self.config['select'])

    def get_action_button_state(self):
        return getattr(pygame, self.config['action'])

    def get_secondary_button_state(self):
        return getattr(pygame, self.config['secondary'])

    def get_escape_button_state(self):
        return getattr(pygame, self.config['escape'])

    
