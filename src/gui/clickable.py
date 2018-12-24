import pygame
import gui.base_component as base_component

    
class Clickable(base_component.BaseComponent):

    def on_click(self, function, *args):
        """Calls a function when ClickableComponent is clicked.
        Note that it is identical to on_hover. The only differences are
        where the function SHOULD be called. This function should be called
        in the input_handling portion of the loop as opposed to on_hover
        which should be called in the render part of the loop."""
        if self.rect.collidepoint(pygame.mouse.get_pos()):
           function(*args)

    def on_hover(self, function, *args):
        """Calls a function when ClickableElement is hovered over with
           the mouse cursor"""
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            function(*args)

    def off_hover(self, function, *args):
        if not self.rect.collidepoint(pygame.mouse.get_pos()):
            function(*args)

    def highlight(self):
        """Highlights VisualElement"""
        highlighted = [x + 30 for x in self.colour if x < 225]
        self.image.fill(highlighted)

    def lowlight(self):
        """Dimmens VisualElement"""
        lowlighted = [x-30 for x in self.colour if x > 30]
        self.image.fill(lowlighted)
