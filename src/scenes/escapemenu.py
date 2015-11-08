import graphics
import gui_base
import pygame
import container_reader
import scenes.scenebase as scene_base
import environment


class EscapeMenu(scene_base.SceneBase):
    """The menu that shows up when a user presses the <ESC> key in game"""

    def __init__(self):
        scene_base.SceneBase.__init__(self)
        self.reader = container_reader.ContainerReader('escape_menu.xml')
        self.component_dict = self.reader.component_dict
        self.components = self.reader.components

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('click')

    def render(self):
        self.component_dict['overlay'].image.fill((0,0,0,100))
        self.components.draw(self.surface)
        pygame.display.flip()
