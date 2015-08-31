import pygame
from constants import *
import environment


   
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

"""
The base container for all other containers to inherit from.
It doesn't do much apart from remove some boilerplate
"""
class BaseContainer(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)


"""A container is a collection of components. Make as many components
as you need. If we need to, we can refactor the container to make it better
but at the moment it serves its purpose."""
class StartContainer(BaseContainer):

    def __init__(self, x, y, width, height):
        self.components = {'start-game' : Clickable(x,y,width,height),
                           'exit-game' : Clickable(x*2,y,width,height),
                           'settings' : Clickable(x*3,y,width,height),
                           'level-select' : Clickable(x*4,y,width,height)} 
    def update(self):
        pass

    def render(self):
        self.components['start-game'].image.fill((255,0,0))
        self.components['start-game'].render_text('START GAME')
        self.components['exit-game'].image.fill((255,255,0))
        self.components['exit-game'].render_text('QUIT')
        self.components['settings'].image.fill((255,0,255))
        self.components['settings'].render_text('SETTINGS')
        self.components['level-select'].image.fill((0,0,255))
        self.components['level-select'].render_text('LEVEL SELECT')
        

class LevelSelectContainer(BaseContainer):

    def __init__(self, x, y, width, height):
        self.components = [Clickable(x,y,width,height) for level in environment.level_obj_list]


class EscapeContainer(BaseContainer):

    def __init__(self, x, y, width, height):
        """
        **Components**
        @resume       : Resumes the game and exits the menu
        @settings     : Takes the user to the settings menu
        @quit-menu    : Quits the game and returns the user to the main menu
        @quit-desktop : Quits the game and returns to the desktop
        """

        self.components = {
                            'resume' : Clickable(x, y, width, height),
                            'settings' : Clickable(x, y, width, height),
                            'quit-menu' : Clickable(x, y, width, height),
                            'quit-desktop' : Clickable(x, y, width, height)
                          } 

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

    
class Clickable(BaseComponent):

    def on_click(self,function, *args):
        """Calls a function when ClickableComponent is clicked.
        Note that it is identical to on_hover. The only differences are
        where the function SHOULD be called. This function should be called
        in the input_handling portion of the loop as opposed to on_hover
        which should be called in the render part of the loop."""
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            function(*args)

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
    @text = The string you want to display
    @size = The size of the font
    @position = The position of the text relative to the surface"""
    def __init__(self,text='Change me',size='12',position=(0,0)):
        self.text = text
        self.size = size
        self.position = position
