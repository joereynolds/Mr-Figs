import pygame

import src.graphics as graphics
import src.entity as entity


class Tile(entity.Entity):
    """The tile class represents any tile in the game background,
        or foreground.
        It extends the entity class
        to add collision mechanics and various other bits"""

    def __init__(self, x, y, width, height, solid, destructable, image=None):
        entity.Entity.__init__(self, x, y, width, height, image)
        self.solid = bool(solid)
        self.destructable = destructable


class FinishTile(Tile):
    def __init__(self, x, y, width, height, solid, destructable, image=None):
        Tile.__init__(self, x, y, width, height, solid, destructable, image)


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
        self.images = [sprite for sprite in graphics.sprites['switch']['sprites']]
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
        self.images = [sprite for sprite in graphics.sprites['laser']['sprites']]

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
