import pygame
import src.entity as entity
import src.colours as colours
import src.graphics as g
from src.countdown_timer import CountdownTimer

# True is teleporting, False is idle
frames =  {
    True: [
        g.subsurf(g.grid(11, 18)),
        g.subsurf(g.grid(12, 18)),
        g.subsurf(g.grid(13, 18)),
        g.subsurf(g.grid(14, 18)),
        g.subsurf(g.grid(15, 18)),
        g.subsurf(g.grid(16, 18)),
        g.subsurf(g.grid(17, 18)),
        g.subsurf(g.grid(18, 18)),
        g.subsurf(g.grid(19, 18)),
        g.subsurf(g.grid(20, 18)),
        g.subsurf(g.grid(21, 18)),
        g.subsurf(g.grid(22, 18)),
    ],
    False: [
        g.subsurf(g.grid(11, 18)),
        g.subsurf(g.grid(12, 18)),
        g.subsurf(g.grid(13, 18)),
        g.subsurf(g.grid(12, 18)),
        g.subsurf(g.grid(11, 18)),
    ]
}

class Portal(entity.Entity):
    """
    When a player collides with this, they are teleported to the x
    and y of the `destination_portal`
    """

    def __init__(self, x, y, width, height, portal_id=None, travels_to_portal_id=None, image=None, destination_portal=None):
        entity.Entity.__init__(self, x, y, width, height, image)

        self.portal_id = portal_id
        self.travels_to_portal_id = travels_to_portal_id
        self.destination_portal = destination_portal

        self.minimap_colour = colours.BROWN_HIGHLIGHT
        self.is_teleporting = False
        self.frame_index = 0
        self.frames = frames
        self.timer = CountdownTimer(0.125)

    def update(self, delta_time):
        self.animate(delta_time)

    def handle_collision(self, tile, player, level):
        if player.destination[0] == self.rect.x and player.destination[1] + player.offset_y == self.rect.y and not player.is_teleporting:
            player.move_player(
                self.destination_portal.rect.x,
                self.destination_portal.rect.y,
            )
            player.is_teleporting = True
            self.is_teleporting = True
            self.destination_portal.is_teleporting = True
        else:
            player.is_teleporting = False
            self.is_teleporting = False
            self.destination_portal.is_teleporting = False

    def animate(self, delta_time):
        self.timer.decrement(delta_time)

        if self.timer.has_ended():
            if self.frame_index >= len(self.frames[self.is_teleporting]) - 1:
                self.frame_index = 0

            self.image = self.frames[self.is_teleporting][self.frame_index]
            
            self.frame_index += 1
            self.timer.reset()
