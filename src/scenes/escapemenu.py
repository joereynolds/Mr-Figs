"""
This module contains the escapemenu class.
The escapemenu is created when a user hits the 'esc' key.
As with all other scenes, it's found in the scenes directory
and uses the escape_menu.xml file for layout
"""

import pygame
import graphics
import gui_base
import environment
import container_reader
import scenes.scenebase as scene_base


class EscapeMenu(scene_base.SceneBase):
    """The menu that shows up when a user presses the <ESC> key in game"""

    def __init__(self):
        scene_base.SceneBase.__init__(self)
        self.reader = container_reader.ContainerReader('escape_menu.xml')
        self.component_dict = self.reader.component_dict
        self.components = self.reader.components
        self.is_open = False

    def is_menu_open(self):
        return self.is_open

    def set_open(self, boolean):
        """Sets the open status of the escape
        menu to a value. This is useful for our click
        handlers since they need to be passed a function
        in order to work
        @boolean should be a...boolean. True or False """
        self.is_open = boolean

    def toggle(self):
        """Toggles the open state of the escape menu.
        This is called in the levelbase's input_handler"""
        self.is_open = not self.is_open

    def process_input(self, event):
        """Processes any input for the escape menu. Note that the iteration
        through all of the events is handled in the GlobalInputHandler so that
        we're only iterating through once"""

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.component_dict['resume'].on_click(
                self.set_open,
                False
            )
            self.component_dict['quit-main'].on_click(
                self.switch_to_scene,
                environment.level_obj_list[1]
            )
            self.component_dict['quit-desktop'].on_click(
                self.terminate,
            )

    def render(self):
        """render a slightly transparent overlay,
        draw the components,
        and render any text on components"""
        self.component_dict['overlay'].image.fill((255, 0, 0, 100))
        self.components.draw(self.surface)

        for component in self.components:
            component.render_text()

            if isinstance(component, gui_base.Clickable):
                #TODO change hover so that we don't have to call 'off hover'.
                #we need to revert back to its previous state when we're
                #no longer hovering
                component.on_hover(
                    component.text.set_color,
                    (255, 0, 0)
                )
                component.off_hover(
                    component.text.set_color,
                    (0, 255, 0)
                )
