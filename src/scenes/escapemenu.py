"""
This module contains the escapemenu class.
The escapemenu is created when a user hits the 'esc' key.
As with all other scenes, it's found in the scenes directory
and uses the escape_menu.xml file for layout
"""

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
        """Toggles the open state of the escape menu. 
        This is called in the levelbase's input_handler"""
        if not self.is_open:
            self.is_open = True
        else :
            self.is_open = False 

    def process_input(self):
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                print('Click')
                self.component_dict['resume'].on_click(
                    print, 'he'        
                )

    def render(self):
        """render a slightly transparent overlay,
        draw the components,
        and render any text on components"""
        self.component_dict['overlay'].image.fill((255,0,0,100))
        self.components.draw(self.surface)
        for component in self.components:
            component.render_text()
        pygame.display.flip()
