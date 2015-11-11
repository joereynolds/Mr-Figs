"""
Contains all events that 
are passed into the event handler
"""
import bomb


def animate_bombs(player):
    """A wrapper to animate all bombs
    that are owned by the player"""
    for bomb in player.bombs:
        bomb.animate()

def animate_particles(player):
    """Another wrapper to animate all
    particles in a bomb"""
    for bomb in player.bombs:
        for particle in bomb.particles:
            pass


"""Old particle animation code to steal from
    self.i = 0 

    def process_input_old(self):
        for event in pygame.event.get():
            if event.type == 29:
                for _bomb in self.player.bombs:
                    for particle in _bomb.particles:
                        particle.image = graphics.sprites['explosion']['sprites'][self.i]
                self.i +=1
                if self.i >5 :
                    self.i = 0
                #This is handled terribly. We should be using delta times for ANY animation. 
                """
