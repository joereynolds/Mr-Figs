from src.game_object.tile import Tile
import src.graphics as graphics

class Triggerable(Tile):
    """A Triggerable class is linked to the Switch or PressurePlate class. It takes a Switch/PressurePlate
       and if that Switch/PressurePlate's state is 'on' it affects the Triggerable and triggers
       whatever the effect of the Triggerable is.

       i.e.
           A Door and switch.
           Door = Triggerable
           Switch = Switch/PressurePlate

           When a switch is pressed, it triggers the door to open...simples!

       @self.stateful = The Stateful that it is linked to
       @self.id = The numeric id of the Triggerable. This is used to link the state and
                  Triggerable together"""

    def __init__(self,x, y, width, height, solid, destructable, stateful, image, id=0):
        self.last_image = 0
        self.image = graphics.sprites['laser']['sprites'][self.last_image]
        Tile.__init__(self, x, y, width, height, solid, destructable, self.image)
        self.stateful = stateful
        self.triggered_id = id
        self.images = graphics.sprites['laser']['sprites']

        self.reverse_animation = False

        # TODO - only play this when the state is on
        # self.laser_hum_sound = pygame.mixer.Sound('./data/audio/fx/laser-hum.ogg')
        # self.laser_hum_sound.play(-1)

    def trigger(self):
        """To be called when our stateful tile is 'on'"""
        if self.stateful.state == 1:
            self.solid = False
            self.image = self.images[0]
        if self.stateful.state == 0:
            self.solid = True
            self.image = graphics.sprites['laser']['sprites'][self.last_image]

    def update(self):
        self.trigger()

    def handle_collision(self, tile, player, level):
        self.update()
        if player.destination[0] == self.rect.x and player.destination[1] == self.rect.y and self.stateful.state == 0:
            pygame.sprite.Sprite.kill(player)

    def animate(self):
        if self.last_image >= 3:
            self.last_image = 0
            self.reverse_animation = True

        if self.last_image <= 0:
            self.last_image = 0
            self.reverse_animation = False

        if self.reverse_animation:
            self.last_image -= 1
        else:
            self.last_image += 1


        self.image = graphics.sprites['laser']['sprites'][self.last_image]