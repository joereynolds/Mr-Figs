import pygame

class EventCommand():
    """Responsible for mapping multiple different devices
    and input types to one universal command. I.e. A controller's
    A button, a keyboards return key and a mouse click all emit
    the same event. Simplifies logic elsewhere.

    We need to define a common grammar for all devices. They have the following

    UP = up
    DOWN = down
    LEFT
    RIGHT
    ACTION
    ESCAPE
    """

    UP = 'up'         # Moving up
    DOWN = 'down'     # Moving down
    LEFT = 'left'     # Moving left
    RIGHT = 'right'   # Moving right
    ESCAPE = 'escape' # Opening up the escape menu
    ACTION = 'action' # Planting a bomb
    NOTHING = 'nothing'

    def __init__(self, controller):
        self.controller = controller

    def map_event_to_command(self, event):
        if event.type == pygame.KEYDOWN:

            if event.key == self.controller.get_up_button_state():
                return {'key': EventCommand.UP, 'raw_event': event}

            if event.key == self.controller.get_down_button_state():
                return {'key': EventCommand.DOWN, 'raw_event': event}

            if event.key == self.controller.get_left_button_state():
                return {'key': EventCommand.LEFT, 'raw_event': event}

            if event.key == self.controller.get_right_button_state():
                return {'key': EventCommand.RIGHT, 'raw_event': event}


            if event.key == self.controller.get_escape_button_state():
                return {'key': EventCommand.ESCAPE, 'raw_event': event}

            if event.key == self.controller.get_action_button_state():
                return {'key': EventCommand.ACTION, 'raw_event': event}

        # TODO - would be nice to merge this with above
        if event.type == pygame.JOYHATMOTION:
            if self.controller.get_up_button_state():
                return {'key': EventCommand.UP, 'raw_event': event}

            if self.controller.get_down_button_state():
                return {'key': EventCommand.DOWN, 'raw_event': event}

            if self.controller.get_left_button_state():
                return {'key': EventCommand.LEFT, 'raw_event': event}

            if self.controller.get_right_button_state():
                return {'key': EventCommand.RIGHT, 'raw_event': event}


        if event.type == pygame.JOYBUTTONDOWN:

            if self.controller.get_action_button_state():
                return {'key': EventCommand.ACTION, 'raw_event': event}

            if self.controller.get_escape_button_state():
                return {'key': EventCommand.ESCAPE, 'raw_event': event}

        if event.type == pygame.MOUSEBUTTONDOWN:
            return {'key': EventCommand.ACTION, 'raw_event': event}


        # If no other event specified, return pygame's event
        return {'key': EventCommand.NOTHING, 'raw_event': event}


