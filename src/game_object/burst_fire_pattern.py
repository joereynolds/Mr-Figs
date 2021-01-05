from src.game_object.bullet import Bullet

class BurstFirePattern():

    def __init__(self, spawn_x: int, spawn_y: int, bullet_speed: int, level, vector):
        self.bullet_timer = 1
        self.time_elapsed = 0
        self.shots_fired = 0
        self.spawn_x = spawn_x
        self.spawn_y = spawn_y
        self.level = level
        self.bullet_speed = bullet_speed
        self.vector = vector

    def fire(self, delta_time):
        """Fires a group of 3 bullets in a burst"""
        self.bullet_timer-= delta_time
        self.time_elapsed += delta_time

        if self.bullet_timer <= 0:
            if self.time_elapsed >= 0.125:
                bullet = Bullet(
                    self.spawn_x,
                    self.spawn_y,
                    2, 
                    2, 
                    self.bullet_speed, 
                    self.vector
                )
                self.level.sprites.add(bullet)
                self.shots_fired += 1
                self.time_elapsed = 0

        if self.shots_fired >= 3:
            self.bullet_timer = 1
            self.shots_fired = 0

