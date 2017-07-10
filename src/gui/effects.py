"""
Contains all of our graphical elements
as well as a few effects for our elements.
"""
import pygame
import graphics
import environment

#TODO each class should have its own file.
   
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
