import pygame
import src.colours as colours
import random
from pygame.math import Vector2
from src.entity import Entity
from src.game_object.particle import Particle
from src.game_object.particle_factory import ParticleFactory

class ParticleEmitter(Entity):

    def __init__(self, x, y, level, emits):
        Entity.__init__(self, x, y, 0, 0, None)
        self.pos = Vector2(x, y)
        self.total = 10
        self.level = level
        self.particles = pygame.sprite.LayeredUpdates()
        self.emits = emits
        self.particle_factory = ParticleFactory(self.rect)

    def create_particle(self) -> Particle:
        return self.particle_factory.build(self.emits)

    def update(self, dt):
        for i in range(self.total):
            if len(self.particles) <= self.total:
                particle = self.create_particle()
                self.particles.add(particle)
                self.level.sprites.add(particle)

        for particle in self.particles:
            if particle.ttl <= 0:
                self.particles.remove(particle)
                self.level.sprites.remove(particle)
