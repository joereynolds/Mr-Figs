import pygame
import graphics
import gui_base
import environment
import container_reader
import scenes.scenebase as scene_base


class StartMenu(scene_base.SceneBase):
    def __init__(self):
        scene_base.SceneBase.__init__(self)
        self.reader = container_reader.ContainerReader('start.xml')
        self.component_dict = self.reader.component_dict
        self.components = self.reader.components

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass 
                self.component_dict['start-game'].on_click(self.switch_to_scene, environment.level_obj_list[2])
                self.component_dict['exit-game'].on_click(self.terminate)
                #self.components['level-select'].on_click(self.switch_to_scene, environment.level_obj_list[1])

    def render(self):
        self.surface.fill((255,255,255))

        self.components.draw(self.surface)

        for component in self.reader.components:
             component.render_text('po')

        pygame.display.flip()



