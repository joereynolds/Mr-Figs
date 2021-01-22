import pygame

from src.game_object.switch_tile import Switch
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

        self.animation_timer = 0.125
        self.frame_index = 0
        self.frames = graphics.sprites['explosion']['sprites']

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
        self.animation_timer -= dt

        if self.animation_timer <= 0:
            if self.last_image >= len(self.frames) - 1:
                self.last_image = 0

            self.last_image += 1
            self.image = self.frames[self.last_image]
            self.animation_timer = 0.125


