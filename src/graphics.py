import pygame
import src.config as config
from src.input_handlers.xbox_360_controller import Xbox360Controller
from src.input_handlers.ps4_controller import PS4Controller
from src.input_handlers.keyboard_controller import KeyboardController
import src.logger as logger

BASE_RESOLUTION = (512, 288)
ZOOM_LEVEL = 1.25

tile_width = 32
tile_height = 32

spritesheet = pygame.image.load(config.spritesheet_location)

def get_controller():
    pygame.joystick.init()

    controller = KeyboardController()
    # TODO - This can be moved to a controller_factory
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        if joystick.get_name() == 'Xbox 360 Controller':
            controller = Xbox360Controller(joystick)
            logger.LOGGER.info("Settings controller to Xbox360Controller")
        if joystick.get_name() == 'Sony Interactive Entertainment Wireless Controller':
            controller = PS4Controller(joystick)
            logger.LOGGER.info("Settings controller to PS4Controller")
        else:

            logger.LOGGER.info(joystick.get_name())
            logger.LOGGER.info("No compatible controller found, falling back to keyboard input")

    return controller

def get_window_surface():
    # TODO - Apparently multiple calls to this are bad? Investigate.
    # return pygame.display.set_mode((512, 288))
    # return pygame.display.set_mode((800, 800))
    return pygame.display.set_mode((0, 0), pygame.NOFRAME)

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
            subsurf(grid(15,11)), # 5
            subsurf(grid(14,11)), # 4 ...
            subsurf(grid(13,11)),
            subsurf(grid(12,11)),
            subsurf(grid(11,11)), # 1
            subsurf(grid(16,11)), # blank bomb 
        ]
    },
    'laser' : {
        'sprites': [
            subsurf(grid(6, 7)), # TODO - waiting on the off laser image to be added to spritesheet
            subsurf(grid(6, 7)),
            subsurf(grid(6, 7)),
            subsurf(grid(6, 7))
        ]
    },
    'switch': {
        'sprites': [subsurf(grid(4, 3)),
                    subsurf(grid(4, 4))]
    },
}
