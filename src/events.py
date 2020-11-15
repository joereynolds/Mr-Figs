"""
Contains all events that 
are passed into the event handler
"""

def call_bomb_events(player):
    animate_bombs(player)
    play_bomb_beeps(player)
    
def animate_bombs(player):
    """A wrapper to animate all bombs
    that are owned by the player"""
    for bomb in player.bombs:
        bomb.animate()

def play_bomb_beeps(player):
    """A wrapper to animate all bombs
    that are owned by the player"""
    for bomb in player.bombs:
        bomb.beep()

def animate_particles(player):
    """Another wrapper to animate all
    particles in a bomb"""
    for bomb in player.bombs:
        for particle in bomb.particles:
            particle.animate()
