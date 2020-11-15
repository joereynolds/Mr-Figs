import pygame
import src.config as config
import src.scenes.scenebase as scene_base
import src.input_handlers.escape_menu_input_handler as input_handler
import src.gui.clickable as clickable

class EscapeMenuNoOverlay(scene_base.SceneBase):
    """The menu that pops up during game when we press escape"""

    def __init__(self):
        scene_base.SceneBase.__init__(self, input_handler.EscapeMenuInput(self)) 

    def render(self):
        pass
    #def render(self):
    #    """Renders all the buttons on our escape menu"""
    #    #TODO honour the alpha value
    #    self.escape_menu_surface.fill((255, 255, 255, 50))
    #    self.surface.blit(self.escape_menu_surface, (0, 0))

    #    self.components.draw(self.surface)
    #    #TODO Maybe this should be in SceneBase?
    #    for component in self.components:
    #        #TODO should just be a call to render() that does everything for us
    #        component.render_text()

    #        if isinstance(component, clickable.Clickable):
    #            #TODO change hover so that we don't have to call 'off hover'.
    #            #we need to revert back to its previous state when we're
    #            #no longer hovering
    #            component.on_hover(
    #                component.text.set_color,
    #                (255, 0, 0)
    #            )
    #            component.off_hover(
    #                component.text.set_color,
    #                (0, 255, 0)
    #            )
