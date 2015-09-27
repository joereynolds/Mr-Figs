import pygame

WIDTH  = 700
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

sprite_width = 16 
sprite_height = 16
spritesheet = pygame.image.load('../data/newtiledsheet.png')

trans_width = 48
trans_height = 48

def grid(x,y):
    """Returns the sprite at the gridded position of n m rather than having to work out the time table for sprite widths!"""
    return sprite_width * x, sprite_height * y 


def subsurf(grid_pos):
    """Quick wrapper around pygame's subsurface so we don't keep having to pass in the width and height"""
    surface = spritesheet.subsurface(grid_pos[0], grid_pos[1], sprite_width, sprite_height) 
    return pygame.transform.scale(surface, (trans_width, trans_height)) 

def interpolate_images(image_from, image_to):
    """Creates an image that is the result of an interpolation between
    @image_from and @image_to	
    @image_from = A pygame surface
    @image_to = A pygame surface"""

    result = pygame.Surface((image_from.get_width(), image_from.get_height())).convert() 

    for y in range(image_from.get_height()):
        for x in range(image_from.get_width()):
            image_from.get_at((x,y))
            image_to.get_at((x,y))
            result.set_at((x,y),(255,255,0))
            #get an intermediate value from these 2 values
    pygame.image.save(result,'bl.png')
image_from = pygame.image.load('../data/test1.png')
image_to = pygame.image.load('../data/test2.png')
interpolate_images(image_from, image_to)

"""

Note that you can't check membership in a tuple if there's only one element (wtf?)

So this:
    if (2,2) in ((2,2))
Doesn't work.
But
    if (2,2) in ((2,2),)
Does...
"""

"""A dictionary of sprites and their properties
    coords = Their location on the spritesheet
    sprites = pygame surfaces of their location
"""
sprites = {
           'wall'   : {
                       'coords' : ((0,1),(0,0),(1,0),(1,1),
                                   (2,0),(3,0),(2,1),(3,1),
                                   (2,3),(1,3),(0,3)),
                      },
           'floor'  : {
                       'coords'  : ((1,2),(0,2)),
                       'sprite_1': subsurf(grid(1,2)),
                       'sprite_2': subsurf(grid(0,2))
                      },
           'bomb'  : {
                       'coords'  : ((0,4),(1,4),(2,4),(3,4),(4,4),(5,4)),
                       'sprites' : [subsurf(grid(0,4)),
                                    subsurf(grid(1,4)),
                                    subsurf(grid(2,4)),
                                    subsurf(grid(3,4)),
                                    subsurf(grid(4,4)),
                                    subsurf(grid(5,4))]
                     },
           'explosion' :{
                         'coords' : (),
                         'sprites':[subsurf(grid(0,6)),
                                    subsurf(grid(1,6)),
                                    subsurf(grid(2,6)),
                                    subsurf(grid(3,6)),
                                    subsurf(grid(4,6)),
                                    subsurf(grid(5,6))]
                        },
           'stair' : {
                       'sprite_1' : subsurf(grid(5,3)),
                     },
           'rock'  : {
                       'coords' : ((2,2),)
                     },
           'player': {
                       'coords' : ((0,5),),
                       'sprites':[subsurf(grid(0,5))]
                     },
           'laser' : {
                       'coords' : ((4,1),(5,1),(6,1),(7,1)),
                       'sprites': [subsurf(grid(4,1)),
                                   subsurf(grid(5,1)),
                                   subsurf(grid(6,1)),
                                   subsurf(grid(7,1))]
                     },
           'switch': {
                        'coords' : ((6,3),(7,3)),
                        'sprites': [subsurf(grid(6,3)),
                                    subsurf(grid(7,3))]
                     }
           }



