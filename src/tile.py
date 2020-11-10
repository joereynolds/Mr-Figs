import pygame

import src.colours as colours
import src.graphics as graphics
import src.entity as entity
from src.movement_vector import vector

class Tile(entity.Entity):
    """The tile class represents any tile in the game background,
        or foreground.
        It extends the entity class
        to add collision mechanics and various other bits"""

    def __init__(self, x, y, width, height, solid, destructable, image=None):
        entity.Entity.__init__(self, x, y, width, height, image)
        self.solid = bool(solid)
        self.destructable = destructable
        
        self.minimap_colour = colours.GREEN

        if self.solid:
            self.minimap_colour = colours.GREEN_BASE

        if self.destructable:
            self.minimap_colour = colours.BROWN_HIGHLIGHT


class MoveableTile(Tile):
    def __init__(self, x, y, width, height, solid, destructable, moveable=False, image=None):
        Tile.__init__(self, x, y, width, height, solid, destructable, image)

    def handle_collision(self, player, level):
        if player.destination[0] == self.rect.x and player.destination[1] == self.rect.y:
            self.rect.x = self.rect.x + (vector[player.direction][0] * graphics.tile_width)
            self.rect.y = self.rect.y + (vector[player.direction][1] * graphics.tile_width)


class FinishTile(Tile):
    def __init__(self, x, y, width, height, solid, destructable, image=None):
        Tile.__init__(self, x, y, width, height, solid, destructable, image)

    def handle_collision(self, player, level):
        if player.destination[0] == self.rect.x and player.destination[1] == self.rect.y:
            level.switch_to_scene(level.next_level)

class Stateful(Tile):
    """The stateful class is a tile that can be either on or off.
       It's a binary state.
       It usually links to the Triggerable class
       so that it can affect (trigger) an effect.

       @self.state    = The starting state of the class
       @self.images   = an array of pygame surfaces
       @self.triggers = The numeric id of the Triggerable
                        if there is one to be triggered"""
    def __init__(self, x, y, width, height, solid, destructable, state, image, triggers=0):
        Tile.__init__(self, x, y, width, height, solid, destructable, image)
        self.state = state
        self.images = graphics.sprites['switch']['sprites']
        self.triggers = triggers

    def update(self):
        self.change_state()

    def change_state(self):
        if self.state:
            self.image = self.images[0]
            self.state = 0
        elif not self.state:
            self.image = self.images[1]
            self.state = 1


class Triggerable(Tile):
    """A Triggerable class is linked to the stateful class. It takes a Stateful
       and if that Stateful's state is 'on' it affects the Triggerable and triggers
       whatever the effect of the Triggerable is.

       i.e.
           A Door and switch.
           Door = Triggerable
           Switch = Stateful

           When a switch is pressed, it triggers the door to open...simples!

       @self.stateful = The Stateful that it is linked to
       @self.id = The numeric id of the Triggerable. This is used to link the state and
                  Triggerable together"""

    def __init__(self,x, y, width, height, solid, destructable, stateful, image, id=0):
        Tile.__init__(self, x, y, width, height, solid, destructable, image)
        self.stateful = stateful
        self.id = id
        self.images = graphics.sprites['laser']['sprites']

        self.laser_hum_sound = pygame.mixer.Sound('./data/audio/fx/laser-hum.wav')
        # self.laser_hum_sound.play(-1)

    def trigger(self):
        """To be called when our stateful tile is 'on'"""
        if self.stateful.state == 1:
            self.solid = False
            self.image = self.images[0]
        if self.stateful.state == 0:
            self.solid = True
            self.image = self.images[1]

    def update(self):
        self.trigger()
