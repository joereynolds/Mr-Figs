import pygame
import environment


class Game(object):

    def __init__(self, fps):

        self.done = False
        self.fps = fps
        self.clock = pygame.time.Clock()

    def run(self, scene):
        """Our main function call. inits pygame, starts our fps clock,
        and then begins our main loop

        @fps = The fps you desire for the program
        @scene = The scene from environment.py that you wish to use
                 for processing
        ,rendering, and updating.
        """
        pygame.init()
        pygame.mixer.init()

        delta_time = 0
        self.clock.tick(self.fps)
        while not self.done:
            scene.process_input()
            scene.update(delta_time)
            scene.render()
            scene = scene.next
            pygame.display.flip()
            delta_time = self.clock.tick(self.fps)/1000.0
        pygame.quit()
