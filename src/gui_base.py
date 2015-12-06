"""
Contains all of our graphical elements
as well as a few effects for our elements.
"""
import pygame
import graphics
import environment

   
def enlarge(self, speed, delta_time):
    """Makes the elements surface larger."""
    speeds = {
        'fast':    10,
        'average': 5,
        'slow':    1
    }

    now = pygame.time.get_ticks()
    if now <= self.cooldown:
        if self.width < self.original_width * 2:
            self.width  += speeds[speed]
            self.height += speeds[speed]
            self.image = pygame.Surface([self.width, self.height]).convert_alpha() 
            self.image.fill(self.colour)
            self.render_text(self.text.text,self.text.position)  

def shrink(self):
    now = pygame.time.get_ticks()
    if now <= self.cooldown:
        if self.width > self.original_width :
            self.width -= 5
            self.height -=5 
            self.image = pygame.Surface([self.width, self.height]).convert_alpha() 
            self.image.fill(self.colour)
            self.render_text(self.text.text, self.text.position)  




#New component system attempt
class BaseComponent(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, string='Default'):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height]).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.text = TextElement(text=string)

    def render_text(self, position = False):
        """Renders text at the default position of (0,0) or otherwise 
        if a position is supplied.
        @text = The text you wish to be displayed
        @position = Position for the text to be rendered (optional)
        """
        if position:
            self.text.position = position
        else: self.text.position = (0,0)

        font_object = pygame.font.Font(None, 20)
        rendered_text = font_object.render(self.text.text,False, self.text.color)
        self.image.blit(rendered_text, self.text.position)

    
class Clickable(BaseComponent):

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
            #self.hovering = True
            function(*args)
        #else:
            #self.hovering = False

    def off_hover(self, function, *args):
        if not self.rect.collidepoint(pygame.mouse.get_pos()):
            function(*args)

    def highlight(self):
        """Highlights VisualElement"""
        highlighted =  [x+30 for x in self.colour if x < 225]
        self.image.fill(highlighted)

    def lowlight(self):
        """Dimmens VisualElement"""
        lowlighted = [x-30 for x in self.colour if x > 30]
        self.image.fill(lowlighted)


class TextElement(pygame.font.Font):
    """Contains all methods and parameters for text.
    @text = The string of text you want to display
    @size = The size of the font
    @position = The position of the text relative to the surface"""
    def __init__(self, text='Change me', size='12', position=(0,0)):
        self.text = text
        self.size = size
        self.color = ((0,255,0))
        self.position = position

    def set_color(self, color):
        self.color = color
