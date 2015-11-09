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
