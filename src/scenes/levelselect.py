import pygame
import gui_base
import graphics
import environment
import container_reader
import scenes.scenebase as scene_base
import input_handlers.level_select_input_handler as input_handler

class LevelMenu(scene_base.SceneBase):

    def __init__(self, levels):
        """
        @levels A dict of our levels that comes from environment.create_level_list
        """
        scene_base.SceneBase.__init__(
            self,
            input_handler.LevelSelectInput(
                self
            )
        )
        self.reader = container_reader.ContainerReader('level_select.xml') 
        self.component_dict = self.reader.component_dict
        self.components = self.reader.components
        self.game_levels = levels

    def render(self):
        """Renders a button for each level that is in the game"""
        self.surface.fill((255, 255, 255))

        self.components.draw(self.surface)
        for component in self.components:
            component.render_text()
