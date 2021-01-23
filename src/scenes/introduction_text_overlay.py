import pygame
import src.graphics as graphics
import src.static_scenes
import src.colours as colours
import src.config as config
import src.scenes.scenebase as scene_base
from src.input_handlers.introduction_input_handler import IntroductionTextOverlayInputHandler
from src.user_data import UserData
from src.resolution_asset_sizer import ResolutionAssetSizer
from src.gui.clickable import Clickable

class IntroductionTextOverlay(scene_base.SceneBase):
    """The menu that pops up during game when we press escape"""

    def __init__(self):
        # TODO needs its own input handler
        self.controller = graphics.get_controller()
        scene_base.SceneBase.__init__(
            self, 
            IntroductionTextOverlayInputHandler(self),
            self.controller
        ) 

        self.user_data = UserData()
        self.screen = graphics.get_window_surface()
        self.screen_surface_rect = self.screen.get_rect()
        self.width, self.height = pygame.display.get_window_size()
        self.center = self.width // 2
        self.surface = pygame.Surface((self.width, self.height)).convert()

        self.size = pygame.display.get_window_size()
        self.asset_sizer = ResolutionAssetSizer()
        self.font_size = self.asset_sizer.get_font_size(self.size)

        pygame.font.init()
        self.font = pygame.font.Font(config.font, self.font_size)
        self.timer = 100
        self.text = """It is time.
            I have studied the Mad Professors schedule
            and can make my escape if I follow the path laid before me.
            I hear from 'The Others' that he's guilty of leaving evidence of these experiments just lying around.
            I should collect these and finally expose his wicked games!"
            """

        self.action_image = self.controller.get_action_button_image()
        self.controller_prompt_x, self.controller_prompt_y = self.screen_surface_rect.midbottom
        self.controller_prompt_x = self.screen_surface_rect.centerx * 0.75
        self.controller_prompt_y -= self.asset_sizer.get_button_size(self.size)[0]

    def render(self):
        """Renders all the buttons on our escape menu"""
        if not self.user_data.get_has_seen_introduction():
            self.timer -= 1
            self.surface.fill(colours.BLACK)
            self.wrap_text(
                self.text, 
                self.font,
                colours.WHITE,
                self.center,
                100,
                self.surface, 
                self.center
            )

            self.screen.blit(self.surface, (0,0))

            rendered_text = self.font.render("Press ", False, colours.WHITE)
            rendered_text_other = self.font.render("To continue ", False, colours.WHITE)

            self.screen.blit(
                rendered_text, 
                (self.controller_prompt_x, self.controller_prompt_y)
            )

            self.screen.blit(
                self.action_image, 
                (self.controller_prompt_x + rendered_text.get_width(), self.controller_prompt_y)
            )

            self.screen.blit(
                rendered_text_other, 
                (
                    self.controller_prompt_x + rendered_text.get_width() + self.action_image.get_width() , 
                    self.controller_prompt_y
                )
            )

        else: 
            self.switch_to_scene(src.static_scenes.level_obj_list['level-select'])


    def wrap_text(self, text: str, font, colour, x, y, screen, allowed_width):
        # first, split the text into words
        words = text.split()

        # now, construct lines out of these words
        lines = []
        while len(words) > 0:
            # get as many words as will fit within allowed_width
            line_words = []
            while len(words) > 0:
                line_words.append(words.pop(0))
                fw, fh = font.size(' '.join(line_words + words[:1]))
                if fw > allowed_width:
                    break

            # add a line consisting of those words
            line = ' '.join(line_words)
            lines.append(line)

        # now we've split our text into lines that fit into the width, actually
        # render them

        # we'll render each line below the last, so we need to keep track of
        # the culmative height of the lines we've rendered so far
        y_offset = 0
        for line in lines:
            fw, fh = font.size(line)

            # (tx, ty) is the top-left of the font surface
            tx = x - fw / 2
            ty = y + y_offset

            font_surface = font.render(line, True, colour)
            screen.blit(font_surface, (tx, ty))

            y_offset += fh
