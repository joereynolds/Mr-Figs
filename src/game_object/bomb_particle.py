import pygame

from src.countdown_timer import CountdownTimer
from src.game_object.switch_tile import Switch
import src.entity as entity
import src.colours as colours
import src.graphics as g

# Keep it out of the class for performance reasons
# we don't want to get subsurfaces everytime we
# create a bomb particle!
sprites = [
    g.subsurf(g.grid(11, 12)),
    g.subsurf(g.grid(12, 12)),
    g.subsurf(g.grid(13, 12)),
    g.subsurf(g.grid(14, 12)),
    g.subsurf(g.grid(15, 12)),
]

class BombParticle(entity.Entity):
    """
    A graphical representation of the explosion surrounding the bomb
    """
    def __init__(self, x, y, width, height):
        self.last_image = 0
        self.image = sprites[self.last_image]
        entity.Entity.__init__(self, x, y, width, height, self.image)
        self.minimap_colour = colours.RED_GLOW

        self.animation_timer = CountdownTimer(0.125)
        self.frame_index = 0
        self.frames = sprites

    def handle_collision(self, tile, player, level):
        for _tile in level.tiled_level.sprites:
            if player.destination[0] == self.rect.x and player.destination[1] + player.offset_y == self.rect.y:
                pygame.sprite.Sprite.kill(player)
                return True
            if isinstance(_tile, Switch):
                if pygame.sprite.collide_rect(self, _tile):
                    _tile.change_state()
                    return

    def update(self, dt):
        self.animate(dt)

    def animate(self, dt):
        self.animation_timer.decrement(dt)

        if self.last_image == len(self.frames) - 1:
            alpha = 128
            self.image.fill((255, 0, 255, alpha), None, pygame.BLEND_RGBA_MULT)
        elif self.animation_timer.has_ended():
            if self.last_image >= len(self.frames) - 1:
                self.last_image = 0

            self.last_image += 1
            self.image = self.frames[self.last_image]
            self.animation_timer.reset()


