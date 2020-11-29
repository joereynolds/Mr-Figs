import pygame

import src.colours as colours
import src.scenes.scenebase as scene_base
import src.input_handlers.start_menu_input_handler as input_handler
from src.gui.clickable import Clickable

class OptionsMenu(scene_base.SceneBase):
    """Options menu for toggling music etc..."""

    def __init__(self):
        scene_base.SceneBase.__init__(
            self,
            # TODO - Own input handler here
            input_handler.StartMenuInput(self)
        )
        self.components = pygame.sprite.LayeredUpdates()

        size = pygame.display.get_window_size()
        self.image = pygame.image.load('./data/background-scene.png')
        self.image = pygame.transform.scale(self.image, (size[0], size[1]))
        center_x = size[0] // 2

        self.components.add([
            Clickable(center_x, 100, 100, 50, '[M]USIC ON/OFF'),
            Clickable(center_x, 200, 100, 50, '[B]ACK'),
        ])

    def render(self):
        """Fill our surface and render our buttons"""
        self.surface.blit(self.image, ((0,0)))
        self.components.draw(self.surface)
        for component in self.components:
            component.render_text()
