import pygame
import environment

def main(fps, scene):
    """Our main function call. inits pygame, starts our fps clock,
    and then begins our main loop

    @fps = The fps you desire for the program
    @scene = The scene from environment.py that you wish to use for processing
    ,rendering, and updating.
    """
    pygame.init()
    pygame.mixer.init()
    done = False
    clock = pygame.time.Clock()

    while not done:
        scene.process_input()
        scene.update()
        scene.render()
        scene = scene.next
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


if __name__ == '__main__':
    main(60,environment.level_obj_list[0])
