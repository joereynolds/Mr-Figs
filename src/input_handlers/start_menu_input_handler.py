"""
Contains our input handler class.
This particular input handler is used for all actions
that aren't player related. i.e. navigating menus
etc...
"""
import src.static_scenes
import pygame
from src.input_handlers.keyboard_controller import KeyboardController
from src.input_handlers.xbox_360_controller import Xbox360Controller
from src.input_handlers.ps4_controller import PS4Controller


# TODO can most menus be generalised?
class StartMenuInput():
    """Handles all inputs for the game itself
    anything related to menu navigation etc...
    is kept in here. All player input is handler
    via the PlayerInputHandler class"""

    def __init__(self, start_menu, controller):
        """
        self.keys is a list of keybindings for each scene
            pygame.K_s: 'level-1',
        Simply means that when we press 's' we will be taken to level-1
        """

        self.start_menu = start_menu
        self.controller = controller

        self.keys = {
            pygame.K_s: 'introduction',
            pygame.K_c: 'credits',
            pygame.K_o: 'options-menu'
        }
        self.last_pressed = (0,0)

    def process_input(self, event):
        """Handles the scenes to go to when we
        click on certain clickable components"""
        if isinstance(self.controller, (PS4Controller, Xbox360Controller)):
            self.process_joystick_input(event)
        else: 
            self.process_keyboard_input(event)

    def process_joystick_input(self, event):
        """Processess all input from a joystick"""
        joystick_movement = self.controller.joystick.get_hat(0)
        button_state = self.controller.get_action_button_state()

        if event.type == pygame.JOYBUTTONDOWN:
            if button_state == 1:
                item = self.start_menu.menu_items.get_selected_item()

                if item.name == 'quit':
                    pygame.quit()
                    return

                item.on_selected(
                    self.start_menu.switch_to_scene,
                    src.static_scenes.level_obj_list[item.name]
                )

        elif joystick_movement != self.last_pressed:
            if joystick_movement != self.controller.keys['nothing']:
                if self.controller.get_down_button_state():
                    self.start_menu.menu_items.select_next_item()
                if self.controller.get_up_button_state():
                    self.start_menu.menu_items.select_previous_item()

            self.last_pressed = joystick_movement
            

    def process_keyboard_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()

            if event.key == pygame.K_DOWN:
                self.start_menu.menu_items.select_next_item()

            if event.key == pygame.K_UP:
                self.start_menu.menu_items.select_previous_item()

            if event.key == pygame.K_RETURN:
                item = self.start_menu.menu_items.get_selected_item()

                if item.name == 'quit':
                    pygame.quit()
                    return

                item.on_selected(
                    self.start_menu.switch_to_scene,
                    src.static_scenes.level_obj_list[item.name]
                )

            for key in self.keys.keys():
                if event.key == key:
                    self.start_menu.switch_to_scene(
                        src.static_scenes.level_obj_list[self.keys[key]]
                    )

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.start_menu.menu_items.items['start-button'].sprite.on_click(
                self.start_menu.switch_to_scene, 
                src.static_scenes.level_obj_list['introduction']
            )

            self.start_menu.menu_items.items['options'].sprite.on_click(
                self.start_menu.switch_to_scene, 
                src.static_scenes.level_obj_list['options-menu']
            )

            self.start_menu.menu_items.items['quit'].sprite.on_click(self.start_menu.terminate)
