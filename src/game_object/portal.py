import pygame
import src.entity as entity
import src.colours as colours

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

    def handle_collision(self, tile, player, level):
        if player.destination[0] == self.rect.x and player.destination[1] + player.offset_y == self.rect.y and not player.is_teleporting:
            player.rect.x = self.destination_portal.rect.x
            player.rect.y = self.destination_portal.rect.y - player.offset_y
            player.destination[0] = self.destination_portal.rect.x
            player.destination[1] = self.destination_portal.rect.y - player.offset_y
            player.is_teleporting = True
        else:
            player.is_teleporting = False
