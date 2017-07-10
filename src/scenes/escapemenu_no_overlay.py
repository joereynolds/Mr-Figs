import pygame
import gui_base
import graphics
import environment
import container_reader
import scenes.scenebase as scene_base

class EscapeMenuNoOverlay(scene_base.SceneBase):

    def __init__(self):
        scene_base.SceneBase.__init__(self)
        self.reader = container_reader.ContainerReader('escape_menu_no_overlay.xml') 
        self.component_dict = self.reader.component_dict
        self.components = self.reader.components


    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.switch_to_scene(environment.level_obj_list[0])

    def render(self):
        """Renders a button for each level that is in the game"""
        self.surface.fill((255, 255, 255))

        self.components.draw(self.surface)
        for component in self.components:
            component.render_text()
