import pygame
import gui_base
import graphics
import environment
import container_reader
import scenes.scenebase as scene_base

class LevelMenu(scene_base.SceneBase):

    def __init__(self):
        scene_base.SceneBase.__init__(self)
        self.reader = container_reader.ContainerReader('level_select.xml') 
        self.component_dict = self.reader.component_dict
        self.components = self.reader.components
        self.game_levels = environment.create_level_list()

    def update(self):
        for event in pygame.event.get():
            for i, level in enumerate(self.components):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    level.on_click(
                        self.switch_to_scene, 
                        self.game_levels[i]
                    )

    def render(self):
        """Renders a button for each level that is in the game"""
        self.surface.fill((255, 255, 255))

        self.components.draw(self.surface)
        for component in self.components:
            component.render_text()
