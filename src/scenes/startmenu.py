import graphics
import gui_base
import pygame
import scenes.scenebase as scene_base
import environment

class StartMenu(scene_base.SceneBase):
    def __init__(self):
        scene_base.SceneBase.__init__(self)
        self.start_container = gui_base.StartContainer(90,90,90,90)
        self.buttons = pygame.sprite.Group()
        self.buttons.add(self.start_container.components['start-game'],
                         self.start_container.components['exit-game'],
                         self.start_container.components['settings'],
                         self.start_container.components['level-select'])
        self.components = self.start_container.components
        

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.components['start-game'].on_click(self.switch_to_scene, environment.level_obj_list[2])
                self.components['exit-game'].on_click(self.terminate)
                self.components['level-select'].on_click(self.switch_to_scene, environment.level_obj_list[1])

    def render(self):
        self.surface.fill((255,255,255))

        self.buttons.draw(self.surface)
        self.start_container.render()

        pygame.display.flip()



