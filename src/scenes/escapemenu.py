import graphics
import gui_base
import pygame
import scenes.scenebase as scene_base
import environment

"""The menu that shows up when a user presses the <ESC> key in game"""
class EscapeMenu(scene_base.SceneBase):
    def __init__(self):
        scene_base.SceneBase.__init__(self)
        self.container= gui_base.EscapeContainer(0,0,graphics.WIDTH,graphics.HEIGHT)
        self.components = pygame.sprite.LayeredUpdates()
        self.components.add(
            self.container.components['overlay'],
            self.container.components['resume'],
            self.container.components['settings'],
            self.container.components['quit-menu'],
            self.container.components['quit-desktop']
        )
        

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('click')

    def render(self):
        self.container.components['overlay'].image.fill((0,0,0,100))
        self.components.draw(self.surface)
        pygame.display.flip()



