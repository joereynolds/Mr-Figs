import pygame
import container_reader
import scenes.scenebase as scene_base
import input_handlers.escape_menu_input_handler as input_handler
import gui.clickable as clickable

class EscapeMenuNoOverlay(scene_base.SceneBase):
    """The menu that pops up during game when we press escape"""

    def __init__(self):
        self.reader = container_reader.ContainerReader('escape_menu_no_overlay.xml') 
        self.component_dict = self.reader.component_dict
        self.components = self.reader.components

        scene_base.SceneBase.__init__(self, input_handler.EscapeMenuInput(self)) 
    def render(self):
        """Renders a button for each level that is in the game"""
        #TODO honour the alpha value
        self.surface.fill((255, 255, 255, 124))

        self.components.draw(self.surface)
        #TODO Maybe this should be in SceneBase?
        for component in self.components:
            #TODO should just be a call to render() that does everything for us
            component.render_text()

            if isinstance(component, clickable.Clickable):
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
