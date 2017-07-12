import entity
import pygame
import graphics
import random

class Bomb(entity.Entity):
    """
    @solid     = Whether the actor can walk through it
    @lifespan  = The amount of steps actor must take before the bomb detonates
    @level     = level data from the LevelEditor class
    @particles = A container for a bomb's particles
    """

    def __init__(self, x, y, width, height, level, lifespan=5, image=None):
        entity.Entity.__init__(self, x, y, width, height, image)
        self.solid = False
        self.lifespan = int(lifespan)
        self.level = level
        self.particles = pygame.sprite.Group()
        self.images = [sprite for sprite in graphics.sprites['bomb']['sprites']]

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
        """Explodes our bomb making sure that the particles only go to the correct boundaries of the walls."""
        for i in range(graphics.trans_width,graphics.trans_width * 4, graphics.trans_width):
            self.create_particle(
                self.rect.x + i, 
                self.rect.y, 
                graphics.trans_width, 
                graphics.trans_height
            )
            self.create_particle(
                self.rect.x - i, 
                self.rect.y, 
                graphics.trans_width, 
                graphics.trans_height
            )
            self.create_particle(
                self.rect.x, 
                self.rect.y + i, 
                graphics.trans_width, 
                graphics.trans_height
            )
            self.create_particle(
                self.rect.x, 
                self.rect.y - i, 
                graphics.trans_width, 
                graphics.trans_height
            )
       
    def create_particle(self,x,y,width,height):
        obj = entity.Entity(
            x,
            y,
            graphics.trans_width,
            graphics.trans_height,
            graphics.sprites['explosion']['sprites'][0]
        )

        #TODO split this code below into a separate function
        try:
            retrieved_tile = self.level.get_tile_from_layer(x,y,1)
            base_tile = self.level.get_tile_from_layer(x,y,0)
            if not base_tile.solid:
                self.particles.add(obj) 
            if retrieved_tile.destructable:
                pygame.sprite.Sprite.kill(retrieved_tile)
        except AttributeError as error:
            print(error)
            print('Attribute Error: Tried to place bomb on non-existent block')
            print(random.random())

    #TODO this should be in the collision handler
    def bomb_collisions(self, bomb_sprite_group):
        """Checks to see if our bomb has touched another bombs explosion. If it has,
        it also explodes"""
        #This might be able to be moved into our collision handler
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


