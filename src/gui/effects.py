"""
Contains any extra effects needed to
be applied on to gui elements
"""

import pygame

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
            self.width += speeds[speed]
            self.height += speeds[speed]
            self.image = pygame.Surface([self.width, self.height])
            self.image.fill(self.colour)
            self.render_text(self.text.text, self.text.position)

def shrink(self):
    """Makes the elements surface smaller."""
    now = pygame.time.get_ticks()
    if now <= self.cooldown:
        if self.width > self.original_width:
            self.width -= 5
            self.height -= 5
            self.image = pygame.Surface([self.width, self.height])
            self.image.fill(self.colour)
            self.render_text(self.text.text, self.text.position)
