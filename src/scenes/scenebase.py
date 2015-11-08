import pygame
import graphics
import container_reader


class SceneBase():
    """The base class for all scenes to inherit from."""

    def __init__(self):
        self.next = self
        self.surface = graphics.SCREEN
        

    def process_input(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def switch_to_scene(self,next_scene):
        self.next = next_scene
        next_scene.next = next_scene

    def terminate(self):
        pygame.quit()


