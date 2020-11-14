import pygame
import src.config as config
from src.save import SaveGame


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
        pygame.display.set_caption(config.game_title)
        # pygame.mixer.pre_init(44100, -16, 2, 512)
        # pygame.mixer.init()
        # pygame.mixer.music.load('./data/audio/music/carmack.ogg')
        # pygame.mixer.music.play(-1)

        delta_time = 0
        self.clock.tick(self.fps)
        while not self.done:
            scene.process_input()
            scene.update(delta_time)
            scene.render()
            scene = scene.next
            pygame.display.flip()
            delta_time = self.clock.tick(self.fps) / 1000.0
        pygame.quit()
