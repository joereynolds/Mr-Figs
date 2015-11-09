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
        self.is_open = False

    def toggle(self):
        if not self.is_open:
            self.is_open = True
        else :
            self.is_open = False 

    def process_input(self):
        for event in pygame.event.get():
            print('event')
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('Click')

    def render(self):
        """render a slightly transparent overlay,
        draw the components,
        and render any text on components"""
        self.surface.fill((250,0,0,100))
        self.components.draw(self.surface)
        for component in self.components:
            component.render_text()
        pygame.display.flip()
