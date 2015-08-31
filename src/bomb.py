import pygame
import tile
import graphics
import entity

"""
@solid     = Whether the actor can walk through it
@lifespan  = The amount of steps actor must take before the bomb detonates
@level     = level data from the LevelEditor class
@particles = A container for a bomb's particles 
"""
class Bomb(entity.Entity):

    def __init__(self, x, y, width, height, level,lifespan=5, image=None):
        entity.Entity.__init__(self, x, y, width, height, image)
        self.solid = False 
        self.lifespan = int(lifespan)
        self.level = level
        self.particles = pygame.sprite.Group()
        self.images = [sprite for sprite in graphics.sprites['bomb']['sprites']]
        
    def __debug(self):
        print(self.lifespan)
        print(type(self.lifespan))

    def blow_up(self):
        """Destroys our bomb and then all of its particles associated with it.
           Returns True on success so that outside classes can know it's completed successfull"""
        if self.lifespan == 0:
            self.explode()
        if self.lifespan <= -1 :
            for particle in self.particles: 
                pygame.sprite.Sprite.kill(particle)
            pygame.sprite.Sprite.kill(self)
            return True

    def explode(self):
        """Explodes our bomb making sure that the particles only go to the correct boundaries of the walls. Or is meant to..."""
        for i in range(graphics.trans_width,graphics.trans_width * 4, graphics.trans_width):
            self.create_particle(self.rect.x + i, self.rect.y, graphics.trans_width, graphics.trans_height)
            self.create_particle(self.rect.x - i, self.rect.y, graphics.trans_width, graphics.trans_height)
            self.create_particle(self.rect.x, self.rect.y + i, graphics.trans_width, graphics.trans_height)
            self.create_particle(self.rect.x, self.rect.y - i, graphics.trans_width, graphics.trans_height)
       
    def create_particle(self,x,y,width,height):
        obj = entity.Entity(x,
                            y,
                            graphics.trans_width,
                            graphics.trans_height,
                            graphics.sprites['explosion']['sprites'][0])
        try:
            retrieved_tile = self.level.get_tile_from_layer(x,y,1)
            base_tile = self.level.get_tile_from_layer(x,y,0)
            if not base_tile.solid:
                self.particles.add(obj) 
            if retrieved_tile.destructable:
                pygame.sprite.Sprite.kill(retrieved_tile)
        except AttributeError:
            print('Attribute Error : Tried to place bomb on non-existent block')
    
    def particle_collision(self, player):
        """Returns True if any of the bombs particles collide with player. If they do, we'll reset the level."""
        for particle in self.particles:
            if pygame.sprite.collide_rect(particle,player) and not player.moving:
                pygame.sprite.Sprite.kill(player)
                return True

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
        if self.image == graphics.sprites['bomb']['sprites'][-1]:
            self.image = self.images[int(-self.lifespan)-1]
	                 #self.images[-self.lifespan-1]
        else:
            self.image = graphics.sprites['bomb']['sprites'][-1]

                       
