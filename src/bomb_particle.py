import pygame

import src.tile as tile
import src.entity as entity
import src.colours as colours
import src.graphics as graphics

class BombParticle(entity.Entity):
    """
    A graphical representation of the explosion surrounding the bomb
    """
    def __init__(self, x, y, width, height):
        image = graphics.sprites['explosion']['sprites'][0]
        entity.Entity.__init__(self, x, y, width, height, image)
        self.minimap_colour = colours.RED_GLOW

    def handle_collision(self, player, level):
        # TODO - There's a bug in here which means that if the player's
        # destination is outside of the particles explosion area then they
        # won't die. This is fine in most cases but it's not accounting for
        # solid. To test it, plant a bomb and move up into a solid wall you'll
        # survive the blast because your destination is in the wall but really
        # you're still on the same tile.
        if player.destination[0] == self.rect.x and player.destination[1] == self.rect.y:
            pygame.sprite.Sprite.kill(player)
            return True
        for _tile in level.tiled_level.sprites:
            if isinstance(_tile, tile.Stateful):
                if pygame.sprite.collide_rect(self, _tile):
                    _tile.update()
                    return


