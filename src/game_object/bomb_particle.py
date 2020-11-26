import pygame

from src.game_object.switch_tile import Switch
import src.game_object.tile as tile
import src.entity as entity
import src.colours as colours
import src.graphics as graphics

class BombParticle(entity.Entity):
    """
    A graphical representation of the explosion surrounding the bomb
    """
    def __init__(self, x, y, width, height):
        self.last_image = 0
        self.image = graphics.sprites['explosion']['sprites'][self.last_image]
        entity.Entity.__init__(self, x, y, width, height, self.image)
        self.minimap_colour = colours.RED_GLOW

    def handle_collision(self, tile, player, level):
        for _tile in level.tiled_level.sprites:
            # TODO - does this need to be in the loop?
            if player.destination[0] == self.rect.x and player.destination[1] == self.rect.y:
                pygame.sprite.Sprite.kill(player)
                return True
            if isinstance(_tile, Switch):
                if pygame.sprite.collide_rect(self, _tile):
                    _tile.update()
                    return

    def animate(self):
        if self.last_image >= 5:
            return

        self.last_image += 1
        self.image = graphics.sprites['explosion']['sprites'][self.last_image]

