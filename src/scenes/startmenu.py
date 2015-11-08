import pygame
import graphics
import gui_base
import environment
import scenes.scenebase as scene_base
import scenes.containers.start_container as container
import container_reader

class StartMenu(scene_base.SceneBase):
    def __init__(self):
        scene_base.SceneBase.__init__(self)
        self.reader = container_reader.ContainerReader()
        self.start_container = container.StartContainer(90,90,90,90)
        self.component_dict = self.start_container.reader.component_dict
        self.components = self.start_container.reader.components
        print(self.components[0])



    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass 
                #self.start.on_click(self.switch_to_scene, environment.level_obj_list[2])
                #self.components['exit-game'].on_click(self.terminate)
                #self.components['level-select'].on_click(self.switch_to_scene, environment.level_obj_list[1])

    def render(self):
        self.surface.fill((255,255,255))

        #self.components.draw(self.surface)
        self.start_container.render()

        pygame.display.flip()



