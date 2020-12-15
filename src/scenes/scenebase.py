import pygame
import src.graphics as graphics


class SceneBase():
    """The base class for all scenes to inherit from."""

    def __init__(self, input_handler):
        """self.next is a sort of 'pointer' to the next level.
        See the environment file for how levels are linked together.
        Essentially we have a linked list of levels.
        
        @input_handler = The input handler for processing input.
                         Each scene has a separate input handler,
                         this allows us to define different key
                         bindings per screen.
                         
                         All levels have 1 input handler
                         The start menu has its own input handler
                         The escape menu has its own input handler
                         """
        self.next = self
        self.surface = graphics.get_window_surface()
        self.input_handler = input_handler

    def process_input(self):
        """Stub for our class that inherit this class"""
        for event in pygame.event.get():
            self.input_handler.process_input(event)

    def update(self, delta_time):
        """Stub for our class that inherit this class"""
        pass

    def render(self):
        """Stub for our class that inherit this class"""
        pass

    def switch_to_scene(self, next_scene):
        """Goes to the next scene. Note that SceneBase is
        sort of similar to a linked list in implementation.
        It is a linked list of scenes"""
        self.next = next_scene
        next_scene.next = next_scene

    def terminate(self):
        """Quit pygame"""
        pygame.quit()
