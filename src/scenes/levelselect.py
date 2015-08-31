import graphics
import gui_base
import pygame
import scenes.scenebase as scene_base
import environment

class LevelMenu(scene_base.SceneBase):
    def __init__(self):
        scene_base.SceneBase.__init__(self)
        self.level_container = gui_base.LevelSelectContainer(90,90,90,90)
        self.buttons = pygame.sprite.Group()
        self.components = self.level_container.components
        

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.components['start-game'].on_click(self.switch_to_scene, environment.level_obj_list[1])
                self.components['exit-game'].on_click(self.terminate)

    def render(self):
        self.surface.fill((255,255,255))

        self.buttons.draw(self.surface)
        pygame.display.flip()


