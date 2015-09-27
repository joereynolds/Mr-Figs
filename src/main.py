import pygame
import environment
import cProfile
import pstats
import io
import sys


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
            #NOTE!
            # This exception handling here is ONLY 
            # for profiling. It hides ALL errors which is BAD BAD BAD.
            # The reason it hides them is so that we can profile without crashing.
            # If you actually want to find out what's wrong with your program,
            # for the love of god remove this exception handling!
            try:
                scene.process_input()
                scene.update()
                scene.render()
                scene = scene.next
                pygame.display.flip()
                clock.tick(self.fps)
            except:
                self.done = True
        pygame.quit()


if __name__ == '__main__':


    game = Game(60)
    pr = cProfile.Profile()
    pr.enable()
    game.run(environment.level_obj_list[0])
    pr.disable()
    log = open('log.test','w')
    sys.stdout = log #redirect all printed output to our text file. This is for profiled information only.
    pr.print_stats()
    log.close()

