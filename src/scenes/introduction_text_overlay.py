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
from src.gui.textbox import Textbox
from src.countdown_timer import CountdownTimer

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
        self.text = [
        """
        Hello. I am Mr Figs.
        At least that's what I call myself.
        I was never given a name.
        What's the point in a name when you're called a number?
        """,
        """
        I was raised in this lab a long time ago.
        I'd like to say things were simpler back then.
        But really... nothing's changed.
        """,
        """
        My days consist of waiting around,
        the occasional unpleasantry,
        and then I go to sleep.
        """,
        """
        It's been like this for years.
        I almost think I'm getting used to it,
        but then I remember where I am.
        """,
        """
        I don't think I can do this much longer.
        It's too easy to waste my life away
        (What's the life expectancy on a weird squid man anyway?).
        I need to break out and fast.
        Perhaps I can spread the news of what this place does to people...
        """,
        """
        It'd be nice if you could follow along to
        make sure I'm safe and that nothing bad happens to me.
        I've seen a lot of this place but it's bigger than you think.

        So what do you say?
        """
        ]

        self.action_image = self.controller.get_action_button_image()
        self.controller_prompt_x, self.controller_prompt_y = self.screen_surface_rect.midbottom
        self.controller_prompt_x = self.screen_surface_rect.centerx * 0.75
        self.controller_prompt_y -= self.asset_sizer.get_button_size(self.size)[0]


        self.image_width, self.image_height = self.asset_sizer.get_button_size(self.size)

        # Scale it up
        zoom = 6
        self.image_width *= zoom
        self.image_height *= zoom
            
        self.animation_timer = CountdownTimer(0.75)

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

        self.textbox = pygame.sprite.GroupSingle(
            Textbox(self.text_blit_coords[0], self.text_blit_coords[1], self.image_width, self.image_height, self.text)
        )

    def update(self, dt):
        self.animate(dt)

    def render(self):
        """Renders all the buttons on our escape menu"""
        if not self.user_data.get_has_seen_introduction():
            self.timer -= 1
            self.surface.fill(colours.BLACK)
            self.textbox.draw(self.surface)

            self.screen.blit(self.surface, (0,0))
            self.textbox.sprite.render(self.screen)
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
            # TODO - switch to the last played level here. Remember where we set off
            self.switch_to_scene(src.static_scenes.level_obj_list['first-level'])


    def animate(self, delta_time):
        self.animation_timer.decrement(delta_time)

        if self.animation_timer.has_ended():

            if self.frame_index >= len(self.frames) - 1:
                self.frame_index = 0

            self.frame_index += 1
            self.animation_timer.reset()
