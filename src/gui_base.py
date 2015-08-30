import pygame
from constants import *


class VisualElement(pygame.sprite.Sprite):
    """The base class for most GUI elements.
       x = int
       y = int
       width = int
       height = int
       color = tuple(int,int,int,int)

       Example

       my_square = VisualElement(50,50,200,200,(0,0,0))

       Creates a black square at x and y of 50 with a 
       width and height of 200"""
   
    def __init__(self,x,y,width,height,colour):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.original_width = width #Used to restore the  the surface back to its original size
        self.height = height
        self.colour = colour
        self.text = TextElement()
        self.image = pygame.Surface([self.width, self.height]).convert_alpha() 
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
        self.cooldown = 7000 #Animation speed 

    def highlight(self):
        """Highlights VisualElement"""
        highlighted =  [x+30 for x in self.colour if x < 225]
        self.image.fill(highlighted)

    def lowlight(self):
        """Dimmens VisualElement"""
        lowlighted = [x-30 for x in self.colour if x > 30]
        self.image.fill(lowlighted)

    def enlarge(self, speed):
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
                self.render_text(self.text.text,self.text.position)  
 


       
#class CheckBox(ClickableElement):
 #   """A checkbox..."""
##
  #  def __init__(self, x, y, width, height, colour):
   #     ClickableElement.__init__(self, x, y, width, height, colour)
    #    self.clicked = False
#
 #   def on_click(self, function, *args):
  #      """Extends the on_click to toggle whether self.clicked is true or false
   #     When it is clicked, we change the icon to a 'clicked' icon"""
    #    if self.rect.collidepoint(pygame.mouse.get_pos()) and not self.clicked:
     #       self.clicked = True
      #      function(*args)
       # else: self.clicked = False

#    def toggle_on(self, function, *args):
 #       """If our checkbox has been toggled in, do this stuff"""
  #      if self.clicked:
   #         function(*args)
#
 #   def toggle_off(self, function, *args):
  #      if not self.clicked:
   #         function(*args)
    


#New component system attempt

"""A container is a collection of components. Make as many components
as you need. If we need to, we can refactor the container to make it better
but at the moment it serves its purpose."""
class StartContainer(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        self.components = {'start-game' : Clickable(x,y,width,height),
                           'exit-game' : Clickable(x*2,y,width,height),
                           'settings' : Clickable(x*3,y,width,height),
                           'level-select' : Clickable(x*4,y,width,height)} 
    def update(self):
        pass

class LevelSelectContainer(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        pass
        #self.components = [Clickable(x,y,width,height for level in level_obj_list)]

class BaseComponent(pygame.sprite.Sprite):

    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height]).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.text = TextElement()

    def render_text(self,text,position = False):
        """Renders text at the default position of (0,0) or otherwise 
        if a position is supplied.
        @text = The text you wish to be displayed
        @position = Position for the text to be rendered (optional)
        """
        if position:
            self.text.position = position
        else: self.text.position = (0,0)

        self.text.text = text
        font_object = pygame.font.Font(None, 20)
        rendered_text = font_object.render(self.text.text,False,((0,0,0)))
        self.image.blit(rendered_text, self.text.position)


class Hoverable(BaseComponent):

    def on_hover(self,function, *args):
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


class Clickable(BaseComponent):

    def on_click(self,function, *args):
        """Calls a function when ClickableComponent is clicked.
        Note that it is identical to on_hover. The only differences are
        where the function SHOULD be called. This function should be called
        in the input_handling portion of the loop as opposed to on_hover
        which should be called in the render part of the loop."""
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            function(*args)


class TextElement(pygame.font.Font):
    """Contains all methods and parameters for text.
    @text = The string you want to display
    @size = The size of the font
    @position = The position of the text relative to the surface"""
    def __init__(self,text='Change me',size='12',position=(0,0)):
        self.text = text
        self.size = size
        self.position = position


