import graphics
import gui_base
import pygame
import scenes.scenebase as scene_base
import environment

class StartMenu(scene_base.SceneBase):
    def __init__(self):
        scene_base.SceneBase.__init__(self)
        self.start_button = gui_base.ClickableElement(50,50,50,50,(150,150,150))
        self.level_button = gui_base.ClickableElement(150,50,50,50,(150,150,150))
        self.exit_button = gui_base.ClickableElement(50,200,50,50,(150,150,150)) 
        self.test_button = gui_base.Container(
                            90,90,90,90,
                            (255,0,0))
        self.buttons = pygame.sprite.Group()
        self.buttons.add(self.start_button,
                         self.exit_button,
                         self.level_button,
                         self.test_button)
        

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.start_button.on_click(self.switch_to_scene, environment.level_obj_list[1])
                self.exit_button.on_click(self.terminate)
            self.test_button.update()

    def render(self):
        self.surface.fill((255,255,255))
        self.test_button.image.fill((255,0,0))
        self.test_button.components['Hoverable'].image.fill((255,0,0))
        self.buttons.draw(self.surface)
        self.start_button.render_text('START')
        self.exit_button.render_text('EXIT')
        pygame.display.flip()



