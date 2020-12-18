"""
This is the thing that mr-figs can stand on and
be moved around on.
"""

import pygame
from pygame.math import Vector2
import src.interpolate as interpolate
from src.game_object.path import Path
import src.entity as entity
import src.colours as colours
import src.graphics as graphics
import time

class Platform(entity.Entity):
    def __init__(
            self, 
            x: int, 
            y: int, 
            width: int, 
            height: int, 
            path: Path, 
            image=None
        ):
        entity.Entity.__init__(self, x, y, width, height, image)
        self.minimap_colour = colours.RED_HIGHLIGHT
        self.path = path
        self.max_speed = 2
        self.position = Vector2(x, y)
        self.waypoint_index = 0
        self.vel = Vector2(0, 0)
        self.target = self.path.points[1]
        self.target_radius = 25
        self.player_on_platform = False
        self.travelling_back = False

    def has_reached_to_destination(self):
        return self.target == self.path.points[0]

    def has_reached_from_destination(self):
        return self.target == self.path.points[-1]

    def pin_player(self, player, x, y):
        """
        Pins the player to x and y.
        Otherwise they wouldn't move
        """
        player.rect.x = x
        player.rect.y = y
        player.destination[0] = x
        player.destination[1] = y

    def handle_collision(self, tile, player, level):
        """
        TODO: this code is shockingly bad. Refactor when less tired and know
        more vector math
        """
        if self.has_reached_to_destination() and not self.player_on_platform:
            self.target = self.path.points[-2]
            self.waypoint_index = (self.waypoint_index - 1) % - len(self.path.points) 
            self.travelling_back = True

        if self.has_reached_from_destination() and not self.player_on_platform:
            self.target = self.path.points[1]
            self.waypoint_index = (self.waypoint_index + 1) % len(self.path.points) 
            self.travelling_back = False

        self.player_on_platform = False
        if player.destination[0] == self.position.x and player.destination[1] == self.position.y:
            self.player_on_platform = True
            player.moving = False

        if self.player_on_platform:
            # We manually change the layer here to the top most one
            # (move_to_front didn't work) so that when we're moving, we're
            # above everything else.
            level.sprites.change_layer(self, 1)


            heading = self.target - self.position
            distance = heading.length()
            heading.normalize_ip()
            player.moving = True

            if self.has_reached_to_destination() and not self.travelling_back:
                self.position.x = self.path.points[-1].x
                self.position.y = self.path.points[-1].y
                self.rect.topleft = self.position
                self.pin_player(player, self.position.x, self.position.y)
                player.moving = False
                return

            if self.has_reached_from_destination() and self.travelling_back:
                self.position.x = self.path.points[0].x
                self.position.y = self.path.points[0].y
                self.rect.topleft = self.position
                self.pin_player(player, self.position.x, self.position.y)
                player.moving = False
                return

            if distance <= 2:  # We're closer than 2 pixels.
                # Increment the waypoint index to swtich the target.
                # The modulo sets the index back to 0 if it's equal to the length.
                if self.travelling_back:
                    self.waypoint_index = (self.waypoint_index - 1) % - len(self.path.points) 
                else:
                    self.waypoint_index = (self.waypoint_index + 1) % len(self.path.points)

                self.target = self.path.points[self.waypoint_index]

            if distance <= self.target_radius:
                self.vel = heading * (distance / self.target_radius * self.max_speed) # If we're approaching the target, we slow down.
            else:  
                self.vel = heading * self.max_speed # Otherwise move with max_speed.

            self.position += self.vel
            self.rect.topleft = self.position
            self.pin_player(player, self.position.x, self.position.y)
