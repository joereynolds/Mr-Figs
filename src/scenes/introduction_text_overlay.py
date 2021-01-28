import pygame
import src.graphics as g
import src.static_scenes
import src.colours as colours
import src.config as config
import src.scenes.scenebase as scene_base
from src.input_handlers.introduction_input_handler import IntroductionTextOverlayInputHandler
from src.user_data import UserData
from src.resolution_asset_sizer import ResolutionAssetSizer
from src.gui.clickable import Clickable

class IntroductionTextOverlay(scene_base.SceneBase):
    """The intro movie"""

    def __init__(self):
        self.controller = g.get_controller()
        scene_base.SceneBase.__init__(
            self, 
            IntroductionTextOverlayInputHandler(self),
            self.controller
        ) 

        self.user_data = UserData()
        self.screen = g.get_window_surface()
        self.screen_surface_rect = self.screen.get_rect()
        self.width, self.height = pygame.display.get_window_size()
        self.center = self.width // 2
        self.surface = pygame.Surface((self.width, self.height)).convert()

        self.size = pygame.display.get_window_size()
        self.asset_sizer = ResolutionAssetSizer()
        self.font_size = self.asset_sizer.get_font_size(self.size, 8)

        pygame.font.init()
        self.font = pygame.font.Font(config.font, self.font_size)
        self.timer = 100
        self.text_index = 0
        self.text = [
        """
        Hello. I am Mr Figs.
        At least that's what I call myself.
        I was never given a name.
        What's the point in a name when you've got noone to call you it?
        """,
        """
        I was raised in this lab a long time ago.
        I'd like to say things were simpler back then.
        But really... nothing's changed.
        """,
        """
        I've been here for years.
        """
        """
        Years.
        I've watched him for years.
        Years as he plucked loved ones from what felt like my grasp.
        Years of screams ringing in my ears and writhing in my mind.
        Years of no purpose.
        """,
        ]

        self.action_image = self.controller.get_action_button_image()
        self.controller_prompt_x, self.controller_prompt_y = self.screen_surface_rect.midbottom
        self.controller_prompt_x = self.screen_surface_rect.centerx * 0.75
        self.controller_prompt_y -= self.asset_sizer.get_button_size(self.size)[0]


        self.image_width, self.image_height = self.asset_sizer.get_button_size(self.size)

        # Scale it up by 4 times
        zoom = 6
        self.image_width *= zoom
        self.image_height *= zoom

        self.animation_timer = 0.750
        self.frame_index = 0
        self.frames = [
            pygame.transform.scale(g.spritesheet.subsurface(0 * g.tile_width, 36 * g.tile_height, g.tile_width, g.tile_height),(self.image_width, self.image_height)),
            pygame.transform.scale(g.spritesheet.subsurface(1 * g.tile_width, 36 * g.tile_height, g.tile_width, g.tile_height),(self.image_width, self.image_height)),
            pygame.transform.scale(g.spritesheet.subsurface(2 * g.tile_width, 36 * g.tile_height, g.tile_width, g.tile_height),(self.image_width, self.image_height)),
            pygame.transform.scale(g.spritesheet.subsurface(3 * g.tile_width, 36 * g.tile_height, g.tile_width, g.tile_height),(self.image_width, self.image_height)),
            pygame.transform.scale(g.spritesheet.subsurface(4 * g.tile_width, 36 * g.tile_height, g.tile_width, g.tile_height),(self.image_width, self.image_height)),
            pygame.transform.scale(g.spritesheet.subsurface(5 * g.tile_width, 36 * g.tile_height, g.tile_width, g.tile_height),(self.image_width, self.image_height)),
        ]

        self.blit_animation_coords = (0, self.height * 0.125)
        self.text_blit_coords = (self.frames[0].get_width(), self.blit_animation_coords[1])

    def update(self, dt):
        self.animate(dt)

    def render(self):
        """Renders all the buttons on our escape menu"""
        # if not self.user_data.get_has_seen_introduction():
        if 1:
            self.timer -= 1
            self.surface.fill(colours.BLACK)
            self.wrap_text(
                self.text[self.text_index], 
                self.font,
                colours.WHITE,
                self.text_blit_coords[0],
                self.text_blit_coords[1],
                self.surface, 
                100
            )

            self.screen.blit(self.surface, (0,0))
            self.screen.blit(self.frames[self.frame_index], (0, self.height * 0.125))

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


    def animate(self, delta_time):
        self.animation_timer -= delta_time

        if self.animation_timer <= 0:

            if self.frame_index >= len(self.frames) - 1:
                self.frame_index = 0

            self.frame_index += 1
            self.animation_timer = 0.750


    def wrap_text(self, text: str, font, colour, x, y, surface, allowed_width):
        # first, split the text into words
        words = text.split("\n")

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
            ty = y + y_offset

            font_surface = font.render(line, True, colour)
            surface.blit(font_surface, (x, ty))

            y_offset += fh
