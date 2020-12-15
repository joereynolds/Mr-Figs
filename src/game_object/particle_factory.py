from src.game_object.particle import Particle
import random
from pygame.math import Vector2

class ParticleFactory():

    def __init__(self, emitter_rect):
        self.emitter_rect = emitter_rect

    def build(self, particle_type: str) -> Particle:
        if particle_type == 'smoke':
            return self.build_smoke_particle()

    def build_smoke_particle(self):
        particle_width = 3
        particle_height = 5
        random_width_offset = random.randint(-particle_width, particle_width)
        random_height_offset = random.randint(-particle_height, particle_height)

        return Particle(
            Vector2(
                self.emitter_rect.centerx + particle_width  + random_width_offset,
                self.emitter_rect.centery - particle_height + random_height_offset
            ),
            particle_width,
            particle_height,
            random.randint(2,8),
            (0,0,0,150)
        )


