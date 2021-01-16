from src.entity import Entity
import src.graphics as graphics
from src.movement_vector import vector

class Player(Entity):

    def __init__(
            self, 
            x: int, 
            y: int, 
            width: int, 
            height: int, 
            image=None
        ):
        self.speed = 2
        self.direction = 'nothing'
        Entity.__init__(self, x, y, width, height, image)

    def update(self, delta_time):
        self.rect.x += self.speed * vector[self.direction][0]
        self.rect.y += self.speed * vector[self.direction][1]
