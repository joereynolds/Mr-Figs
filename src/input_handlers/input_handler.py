"""
Contains our input handler class.
This particular input handler is used for all actions
that aren't player related. i.e. navigating menus
etc...
"""
import src.game_object.solid_tile
from src.scenes.startmenu import StartMenu
import src.static_scenes
import pygame


class InputHandler():
    """Handles all inputs for the game itself
    anything related to menu navigation etc...
    is kept in here. All player input is handler
    via the PlayerInputHandler class"""

    def __init__(self, player, level, controller):
        """
        @self.player = The player on the level
        @self.level  = The Base level.
                       This is needed to access functions that aren't
                       available in the TiledMap object
        """
        self.player = player
        self.level = level
        self.controller = controller
        self.last_pressed = (0,0)

    def process_input(self, event):
        """Processes therelated actions that are present in self.keys.
        self.keys is a mapping of keyboard input to a function.
        Note also that if we're not pressing the spacebar then we want
        to update everything in the game. The reason being is that we
        don't want to update things when we plant a bomb (press spacebar)"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                self.level.switch_to_scene(self.level.tiled_level.properties['next_level'])
            if event.key == pygame.K_q:
                self.level.switch_to_scene('start-menu', True)
            if event.key == pygame.K_ESCAPE:
                self.level.renderer.escape_menu.toggle_visiblity()
            if event.key == pygame.K_r:
                self.level.reset()
            if event.key == pygame.K_RETURN:
                item = self.level.renderer.escape_menu.menu_items.get_selected_item()
                if item.name == 'continue':
                    self.level.renderer.escape_menu.close_menu()
                if item.name == 'restart':
                    self.level.reset()
                if item.name == 'main':
                    self.level.switch_to_scene('start-menu', True)
                if item.name == 'quit':
                    pygame.quit()

            if event.key == pygame.K_c:
                self.level.renderer.escape_menu.close_menu()
            if event.key == pygame.K_UP:
                self.level.renderer.escape_menu.menu_items.select_previous_item()
            if event.key == pygame.K_DOWN:
                self.level.renderer.escape_menu.menu_items.select_next_item()

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.level.renderer.escape_menu.menu_items.items['continue'].sprite.on_click(
                print,
                "CON"
            )
            self.level.renderer.escape_menu.menu_items.items['restart'].sprite.on_click(
                print,
                "RES"
            )

    def process_joystick_input(self, event):
        """Processes therelated actions that are present in self.keys.
        self.keys is a mapping of keyboard input to a function.
        Note also that if we're not pressing the spacebar then we want
        to update everything in the game. The reason being is that we
        don't want to update things when we plant a bomb (press spacebar)"""
        joystick_movement = self.controller.joystick.get_hat(0)
        button_state = self.controller.get_action_button_state()

        if event.type == pygame.JOYBUTTONDOWN:
            if self.controller.get_start_button_state():
                self.level.renderer.escape_menu.toggle_visiblity()
            if self.controller.get_y_button_state():
                self.level.reset()

            if button_state == 1:
                item = self.level.renderer.escape_menu.menu_items.get_selected_item()

                if item.name == 'quit':
                    pygame.quit()
                    return

                if item.name == 'continue':
                    self.level.renderer.escape_menu.close_menu()

                if item.name == 'restart':
                    self.level.reset()

                if item.name == 'main':
                    self.level.switch_to_scene('start-menu', True)

        elif joystick_movement != self.last_pressed:
            if joystick_movement != self.controller.keys['nothing']:
                if self.controller.get_down_button_state():
                    self.level.renderer.escape_menu.menu_items.select_next_item()
                if self.controller.get_up_button_state():
                    self.level.renderer.escape_menu.menu_items.select_previous_item()

            self.last_pressed = joystick_movement
