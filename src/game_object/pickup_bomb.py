import pygame
import src.entity as entity
import src.colours as colours

class PickupBomb(entity.Entity):
    """The tile class represents any tile in the game background,
        or foreground.
        It extends the entity class
        to add collision mechanics and various other bits"""

    def __init__(self, x, y, width, height, image=None):
        entity.Entity.__init__(self, x, y, width, height, image)

        self.minimap_colour = colours.GREEN

    def handle_collision(self, tile, player, level):
        if player.destination[0] == self.rect.x and player.destination[1] == self.rect.y:
            player.add_bomb()
            pygame.sprite.Sprite.kill(self)
