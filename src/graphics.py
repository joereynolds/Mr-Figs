import pygame
import src.config as config
from src.input_handlers.xbox_360_controller import Xbox360Controller
from src.input_handlers.keyboard_controller import KeyboardController

BASE_RESOLUTION = (512, 288)
ZOOM_LEVEL = 1.5

tile_width = 16
tile_height = 16

def get_controller():
    pygame.joystick.init()

    controller = KeyboardController
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        if joystick.get_name() == 'Xbox 360 Controller':
            controller = Xbox360Controller(joystick)
        else:
            logger.LOGGER.info("No compatible controller found, falling back to keyboard input")

    return controller
            



def get_window_surface():
    # return pygame.display.set_mode((768, 768), )
    return pygame.display.set_mode((800, 480), )
    # return pygame.display.set_mode((768, 768), )
    # return pygame.display.set_mode((640, 480), )
    # return pygame.display.set_mode((1280, 960), )
    # return pygame.display.set_mode((1920, 1080), )
    return pygame.display.set_mode((0, 0), pygame.NOFRAME)
    # return pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def grid(x: int, y: int):
    """
    Returns the sprite at the gridded position of n m rather
    than having to work out the time table for sprite widths!
    """
    return tile_width * x, tile_height * y

def subsurf(grid_pos):
    """
    Quick wrapper around pygame's subsurface so we don't keep having to pass in the width and height
    """
    spritesheet = pygame.image.load(config.spritesheet_location)
    return spritesheet.subsurface(grid_pos[0], grid_pos[1], tile_width, tile_height)


"""A dictionary of sprites and their properties
    sprites = pygame surfaces of their location
"""
# TODO - These should be moved into the class responsible for them
sprites = {
    'bomb'  : {
        'sprites' : [
            subsurf(grid(0,4)),
            subsurf(grid(1,4)),
            subsurf(grid(2,4)),
            subsurf(grid(3,4)),
            subsurf(grid(4,4)),
            subsurf(grid(5,4))
        ]
    },
    'explosion' :{
        'sprites':[
            subsurf(grid(0, 6)),
            subsurf(grid(1, 6)),
            subsurf(grid(2, 6)),
            subsurf(grid(3, 6)),
            subsurf(grid(4, 6)),
            subsurf(grid(5, 6))
        ]
    },
    'player': {
        'sprites':[subsurf(grid(0,5))]
    },
    'laser' : {
        'sprites': [
            subsurf(grid(4, 1)),
            subsurf(grid(5, 1)),
            subsurf(grid(6, 1)),
            subsurf(grid(7, 1))
        ]
    },
    'switch': {
        'sprites': [subsurf(grid(6, 3)),
                    subsurf(grid(7, 3))]
    },
    'pressure_plate': {
        'sprites': [
            # These are both the same surface for now
            # I don't have an image for a pressure_plate in the 'on'
            # position yet.
            subsurf(grid(8, 5)),
            subsurf(grid(8, 5)),
        ]
    }
}
