import pygame
import environment


class Game():

    def __init__(self, fps):

        self.done = False
        self.fps = fps

    def run(self, scene):
        """Our main function call. inits pygame, starts our fps clock,
        and then begins our main loop

        @fps = The fps you desire for the program
        @scene = The scene from environment.py that you wish to use for processing
        ,rendering, and updating.
        """ 
        pygame.init()
        pygame.mixer.init()
        clock = pygame.time.Clock()

        while not self.done:
            scene.process_input()
            scene.update()
            scene.render()
            scene = scene.next
            pygame.display.flip()
            clock.tick(self.fps)
        pygame.quit()

    def run_mock(self,scene):
        """Identical to our run except this method implements
        a mock AI to run through the game for us and look for bugs.
        very useful!"""

        pygame.init()
        pygame.mixer.init()
        clock = pygame.time.Clock()

        while not self.done:
            scene.process_input()
            scene.update()
            scene.render()
            scene = scene.next
            pygame.display.flip()
            clock.tick(self.fps)
        pygame.quit()
