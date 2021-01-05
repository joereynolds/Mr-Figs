
class Xbox360Controller():

    NAME = 'Xbox 360 Controller'

    keys = {
        # buttons
        0: 'nothing',
        1: 'space',

        #hats (dpad)
        (1, 0): 'right',
        (-1, 0): 'left',
        (0, 1): 'up',
        (0, -1): 'down',
        (0, 0): 'nothing',

        # Weird in between values, just try and guess them best we can
        (1, 1): 'up',
        (-1, 1): 'up',
        (1, -1): 'down',
        (-1, -1): 'down',

        # Occasionally we want to map back so we provide these too
        'nothing': (0, 0),
    }

    def __init__(self, joystick):
        self.joystick = joystick

    def get_a_button_state(self):
        """Gets the state of the A button"""
        return self.joystick.get_button(0)

    def get_y_button_state(self):
        """Gets the state of the A button"""
        return self.joystick.get_button(3)

    def get_start_button_state(self):
        return self.joystick.get_button(7)
