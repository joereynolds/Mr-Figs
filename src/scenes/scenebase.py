import pygame
import graphics
import container_reader


class SceneBase():
    """The base class for all scenes to inherit from."""

    def __init__(self):
        self.next = self
        self.surface = graphics.SCREEN
        
    def process_input(self):
        """Stub for our clas that inherit this class"""
        pass

    def update(self):
        """Stub for our clas that inherit this class"""
        pass

    def render(self):
        """Stub for our clas that inherit this class"""
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


