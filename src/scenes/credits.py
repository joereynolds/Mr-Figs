import pygame
import src.graphics as graphics
import src.static_scenes
import src.colours as colours
import src.config as config
import src.scenes.scenebase as scene_base
import src.input_handlers.escape_menu_input_handler as input_handler
from src.user_data import UserData
from src.gui.clickable import Clickable

class Credits(scene_base.SceneBase):
    """The menu that pops up during game when we press escape"""

    def __init__(self):
        # TODO needs its own input handler
        scene_base.SceneBase.__init__(
            self, 
            input_handler.EscapeMenuInput(self),
            graphics.get_controller()
            ) 

        self.user_data = UserData()
        self.screen = graphics.get_window_surface()
        self.width, self.height = pygame.display.get_window_size()
        self.center = self.width // 2
        self.surface = pygame.Surface((self.width, self.height)).convert()
        self.font_size = 24
        pygame.font.init()
        self.font = pygame.font.Font(config.font, self.font_size)
        self.timer = 150
        self.credits = [
            "Created by: Me",
            "Music by: Me",
            "Level Design: Me + ...",
            "Art: ..."
        ]

    def render(self):
        """Renders all the buttons on our escape menu"""
        if self.timer > 0:
            self.timer -= 1
            self.surface.fill(colours.BLACK)

            for i, credit in enumerate(self.credits):
                rendered_text = self.font.render(credit, False, colours.WHITE)
                rendered_text_rect = rendered_text.get_rect(center=(self.width // 2, self.height // 2 + (i * self.font.get_height())))
                self.surface.blit(rendered_text, rendered_text_rect)

            self.screen.blit(self.surface, (0,0))
        else:
            self.timer = 100
            self.switch_to_scene(src.static_scenes.level_obj_list['start-menu'])
