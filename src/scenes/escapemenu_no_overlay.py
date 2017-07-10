import pygame
import gui_base
import graphics
import environment
import container_reader
import scenes.scenebase as scene_base

class EscapeMenuNoOverlay(scene_base.SceneBase):

    def __init__(self):
        scene_base.SceneBase.__init__(self)
        self.reader = container_reader.ContainerReader('escape_menu_no_overlay.xml') 
        self.component_dict = self.reader.component_dict
        self.components = self.reader.components


    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.component_dict['resume'].on_click(
                    self.switch_to_scene,
                    environment.level_obj_list[3]
                )
                self.component_dict['quit-main'].on_click(
                    self.switch_to_scene,
                    environment.level_obj_list[1]
                )
                self.component_dict['quit-desktop'].on_click(
                    self.terminate,
                )

    def render(self):
        """Renders a button for each level that is in the game"""
        self.surface.fill((255, 255, 255))

        self.components.draw(self.surface)
        for component in self.components:
            #TODO should just be a call to render() that does everything for us
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
