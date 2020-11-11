"""
Everything related to the bomb that mr-figs drops.
"""

import pygame

from src.tile import MoveableTile
from src.entity import Entity
from src.bomb_particle import BombParticle
import src.graphics as graphics
import src.logger as logger
import src.colours as colours
from pprint import pprint


class Bomb(Entity):
    """
    @lifespan  = The amount of steps actor must take before the bomb detonates
    @level     = level data from the LevelEditor class
    @particles = A container for a bomb's particles
    """

    def __init__(self, x, y, width, height, level, lifespan=5, image=None):
        Entity.__init__(self, x, y, width, height, image)
        self.lifespan = int(lifespan)
        self.tiled_level = level
        self.particles = pygame.sprite.Group()
        self.images = graphics.sprites['bomb']['sprites']

        self.bomb_creation_sound = pygame.mixer.Sound('./data/audio/fx/bomb-place.wav')
        self.bomb_beep_sound = pygame.mixer.Sound('./data/audio/fx/bomb-beep.wav')

        self.bomb_explosion_sound = pygame.mixer.Sound('./data/audio/fx/bomb-explode.wav')
        self.bomb_explosion_sound.set_volume(0.2)

        self.bomb_creation_sound.play()

        self.minimap_colour = colours.BLACK

    #TODO two methods, one called blow_up, one called explode it's confusing
    def blow_up(self):
        """Destroys our bomb and then all of its particles associated with it.
           Returns True on success so that outside classes can know it's completed successfully"""
        if self.lifespan == 0:
            self.explode()
        if self.lifespan <= -1:
            for particle in self.particles:
                pygame.sprite.Sprite.kill(particle)
            pygame.sprite.Sprite.kill(self)
            return True

    def explode(self):
        """
        Explodes our bomb making sure that the particles
        only go to the correct boundaries of the walls.
        """
        for i in range(graphics.tile_width, graphics.tile_width * 4, graphics.tile_width):
            right = self.rect.x + i
            
            has_created_particle = self.create_particle(
                right,
                self.rect.y,
                graphics.tile_width,
                graphics.tile_height
            )

            if not has_created_particle:
                break

        for i in range(graphics.tile_width, graphics.tile_width * 4, graphics.tile_width):
            left = self.rect.x - i

            has_created_particle = self.create_particle(
                left,
                self.rect.y,
                graphics.tile_width,
                graphics.tile_height
            )

            if not has_created_particle:
                break

        for i in range(graphics.tile_width, graphics.tile_width * 4, graphics.tile_width):
            down = self.rect.y + i

            has_created_particle = self.create_particle(
                self.rect.x,
                down,
                graphics.tile_width,
                graphics.tile_height
            )

            if not has_created_particle:
                break

        for i in range(graphics.tile_width, graphics.tile_width * 4, graphics.tile_width):
            up = self.rect.y - i

            has_created_particle = self.create_particle(
                self.rect.x,
                up,
                graphics.tile_width,
                graphics.tile_height
            )

            if not has_created_particle:
                break

        # TODO Not a fan of this explosion sound, get another one 
        # self.bomb_explosion_sound.play()

    def create_particle(self, x, y, width, height):
        created = False

        particle = BombParticle(
            x,
            y,
            width,
            height,
        )

        tile_object = self.tiled_level.get_tile_from_object_layer(x, y)
        base_tile = self.tiled_level.get_tile_from_layer(x, y, 0)

        if tile_object and tile_object.type == 'moveable_tile':
            return False

        self.particles.add(particle)
        created = True

        if tile_object and tile_object.destructable:
            pass
            # self.tiled_level.sprites.remove(tile_object)
            # Remove the tile_object from the sprites
            # self.tiled_level.sprites.remove(tile_object)
            # pygame.sprite.Sprite.kill(tile_object)

        return created

    def bomb_collisions(self, bomb_sprite_group):
        """Checks to see if our bomb has touched another bombs explosion. If it has,
        it also explodes"""
        for bomb in bomb_sprite_group:
            if bomb != self:
                for particle in bomb.particles:
                    if pygame.sprite.collide_rect(self, particle):
                        self.lifespan = bomb.lifespan #remember to detonate both bombs at the same time!`
                        self.explode()

    def animate(self):
        """Switches the images of our bomb sprite depending
        on the bomb's lifespan"""
        if self.image == graphics.sprites['bomb']['sprites'][-1]:
            self.image = self.images[int(-self.lifespan)-1]
        else:
            self.image = graphics.sprites['bomb']['sprites'][-1]

    def beep(self):
        """
        Plays the bombs beep sound
        """
        self.bomb_beep_sound.play()
