import pygame

class PlayerInputHandler():
    """Handles all input processing for players.
    This is meant to be extendable so that in theory,
    we can pass this class to 400 players and they could
    all handle their input with minimal extra effort from me."""

    def __init__(self, player, level, controller=None):
        self.player = player
        self.level = level
        self.controller = controller
        self.last_pressed = (0,0)

    def process_input(self, event):
        """Processess all input from a keyboard"""
        for key, action in self.controller.keys.items():
            if event.key == key:
                self.player.event_update(action)
                self.level.turn_based_collision_handler.update()
                self.player.add_turn()

    def process_joystick_input(self, event):
        """Processess all input from a joystick"""
        joystick_movement = self.controller.joystick.get_hat(0)
        button_state = self.controller.get_a_button_state()

        if event.type == pygame.JOYBUTTONDOWN:
            if button_state == 1:
                self.player.event_update(
                    self.controller.keys[button_state]
                )
                self.last_pressed = joystick_movement
                self.level.turn_based_collision_handler.update()
        elif joystick_movement != self.last_pressed:
            if joystick_movement != self.controller.keys['nothing']:
                self.player.event_update(
                    self.controller.keys[joystick_movement]
                )
                self.level.turn_based_collision_handler.update()
                self.player.add_turn()

            self.last_pressed = joystick_movement

