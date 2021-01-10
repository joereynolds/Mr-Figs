import pygame

import src.colours as colours
from src.entity import Entity
from pathlib import Path

class VideoTape(Entity):
    """The tile class represents any tile in the game background,
        or foreground.
        It extends the entity class
        to add collision mechanics and various other bits"""

    def __init__(
            self, 
            x: int, 
            y: int, 
            width: int, 
            height: int, 
            story: str, 
            image=None
        ):
        Entity.__init__(self, x, y, width, height, image)
        self.text = Path(story).read_text()

        """When we view a video we want to go *back* to where we came
        we use this. Currently we do this in the code but we should
        move it to Tiled when we get a chance"""
        self.redirect_to = None

        self.minimap_colour = colours.WHITE

    def handle_collision(self, tile, player, level):
        if player.destination[0] == self.rect.x and player.destination[1] == self.rect.y:
            level.renderer.display_video_tape_story(self)
            pygame.sprite.Sprite.kill(self)
