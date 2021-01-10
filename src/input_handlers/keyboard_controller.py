import pygame

class KeyboardController():

    def get_down_button_state():
        return pygame.K_DOWN

    def get_up_button_state():
        return pygame.K_UP

    def get_left_button_state():
        return pygame.K_LEFT

    def get_right_button_state():
        return pygame.K_RIGHT

    def get_select_button_state():
        return pygame.K_RETURN

    def get_action_button_state():
        return pygame.K_SPACE

    def get_escape_button_state():
        return pygame.K_ESCAPE
