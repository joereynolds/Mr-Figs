import pygame

class Clock():

    def __init__(self):
        self.clock = pygame.time.Clock() 
        self.birth_time = self.clock.get_time()

    def call_n_seconds(self, function, *args):
        """Calls a function in n seconds"""
        pass
    
