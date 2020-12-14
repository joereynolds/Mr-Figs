from src.game_object.triggerable import Triggerable
from src.game_object.barrel import Barrel
"""
Contains all events that 
are passed into the event handler
"""

def call_bomb_events(player, level=None):
    animate_bombs(player)
    play_bomb_beeps(player)
    
def animate_bombs(player, level=None):
    """A wrapper to animate all bombs
    that are owned by the player"""
    for bomb in player.bombs:
        bomb.animate()

def animate_lasers(player, level):
    for sprite in level.tiled_level.sprites:
        if isinstance(sprite, Triggerable):
            sprite.animate()

def play_bomb_beeps(player, level=None):
    """A wrapper to animate all bombs
    that are owned by the player"""
    for bomb in player.bombs:
        bomb.beep()

def animate_particles(player, level=None):
    """Another wrapper to animate all
    particles in a bomb"""
    for bomb in player.bombs:
        for particle in bomb.particles:
            particle.animate()

def command_barrels_to_shoot(player=None, level=None):
    for sprite in level.tiled_level.sprites:
        if isinstance(sprite, Barrel):
            sprite.shoot(level)
