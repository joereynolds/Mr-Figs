import pygame
import graphics
import entity

class Bomb(entity.Entity):

    def __init__(self, x, y, width, height, level, image=None):
        entity.Entity.__init__(self, x, y, width, height, image)
        self.solid = True 
        self.lifespan = 5 #How many steps the player has to take until the bom blows up
        self.level = level
        self.particles = pygame.sprite.Group() #container for our particles

    def blow_up(self):
        if self.lifespan ==0:
            self.explode()
        if self. lifespan <= -2:
            for particle in self.particles: 
                pygame.sprite.Sprite.kill(particle)
            pygame.sprite.Sprite.kill(self)
            return True

    def explode(self):
        """Explodes our bomb making sure that the particles only go to the correct boundaries of the walls. Or is meant to..."""
        #Create bombs to the (eventual left) and right of the original bomb
        #...who needs algorithms...
        self.create_particle(self.rect.x + 50, self.rect.y, 50, 50)
        self.create_particle(self.rect.x + 100, self.rect.y, 50, 50)
        self.create_particle(self.rect.x + 150, self.rect.y, 50, 50)
        self.create_particle(self.rect.x + 200, self.rect.y, 50, 50)
        self.create_particle(self.rect.x - 50, self.rect.y, 50, 50)
        self.create_particle(self.rect.x - 100, self.rect.y, 50, 50)
        self.create_particle(self.rect.x - 150, self.rect.y, 50, 50)
        self.create_particle(self.rect.x - 200, self.rect.y, 50, 50)

        self.create_particle(self.rect.x, self.rect.y + 50, 50, 50)
        self.create_particle(self.rect.x, self.rect.y + 100, 50, 50)
        self.create_particle(self.rect.x, self.rect.y + 150, 50, 50)
        self.create_particle(self.rect.x, self.rect.y + 200, 50, 50)
        self.create_particle(self.rect.x, self.rect.y - 50, 50, 50)
        self.create_particle(self.rect.x, self.rect.y - 100, 50, 50)
        self.create_particle(self.rect.x, self.rect.y - 150, 50, 50)
        self.create_particle(self.rect.x, self.rect.y - 200, 50, 50)
       
    def create_particle(self,x,y,width,height):
        obj = entity.Entity(x,y,50,50)
        try:
            if not self.level.get_tile(x,y).solid:#Check to make sure we're not trying to put a particle on a solid block
                self.particles.add(obj) 
            elif self.level.get_tile(x,y).destructable:
                #If it's destructable, kill it and change its attributes
                self.level.get_tile(x,y).image = graphics.spritesheet.subsurface(466,68,50,50)
                self.level.get_tile(x,y).solid = False
                self.level.get_tile(x,y).destructable = False 
        except AttributeError:
            print('Attribute Error : Tried to place tile on non-existent block')

