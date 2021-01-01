"""
NOTE: This file isn't used but it'd be nice to switch to it when possible
Contains our input handler class.
This particular input handler is used for all actions
that aren't player related. i.e. navigating menus
etc...
"""
import src.static_scenes
import pygame


class EscapeMenuInput():
    """Handles all inputs for the game itself
    anything related to menu navigation etc...
    is kept in here. All player input is handler
    via the PlayerInputHandler class"""

    def __init__(self, escape_menu):
        self.escape_menu = escape_menu


    def process_input(self, event):
        """Handles the scenes to go to when we
        click on certain clickable components"""
        pass
