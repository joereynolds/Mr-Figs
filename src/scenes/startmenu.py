import pygame
import graphics
import gui_base
import environment
import container_reader
import scenes.scenebase as scene_base
import input_handlers.start_menu_input_handler as input_handler

class StartMenu(scene_base.SceneBase):
    """Initial start menu at the start of the game"""

    def __init__(self):
        scene_base.SceneBase.__init__(
            self,
            input_handler.StartMenuInput(self)
        )
        self.reader = container_reader.ContainerReader('start.xml')
        self.component_dict = self.reader.component_dict
        self.components = self.reader.components

    def render(self):
        self.surface.fill((255, 255, 255))
        self.components.draw(self.surface)
        for component in self.components:
            component.render_text()
