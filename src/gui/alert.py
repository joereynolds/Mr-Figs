import pygame
import src.graphics as graphics
import src.config as config
import src.colours as colours

import src.scenes.scenebase as scene_base
from src.input_handlers.alert_input_handler import AlertInput
from src.resolution_asset_sizer import ResolutionAssetSizer
from src.gui.clickable import Clickable
from src.gui.menu_items import MenuItems

class Alert():

    def __init__(
            self, 
            prompt: str, 
            done_message: str,
            confirm_action, 
            *args
        ):
        self.prompt = prompt
        self.confirm_action = confirm_action
        self.args = args if args else None
        self.input_handler = AlertInput(self)

        self.has_confirmed = False
        self.is_visible = False
        self.width, self.height = pygame.display.get_window_size()
        self.surface = pygame.Surface((self.width // 2, self.height // 2)).convert_alpha()
        self.rect = self.surface.get_rect()
        asset_sizer = ResolutionAssetSizer()
        self.button_width, self.button_height = asset_sizer.get_button_size((self.width, self.height))

        left = self.rect.left + self.button_width

        self.button_width *= 3
        self.button_height *= 2

        offset = self.button_height
        bottom = self.rect.bottom

        self.text = done_message
        self.font_size = asset_sizer.get_font_size(
            pygame.display.get_window_size()
        )

        self.font = pygame.font.Font(config.font, self.font_size)

        items = {
            'cancel': pygame.sprite.GroupSingle(
                Clickable(
                    left, 
                    bottom - offset,
                    self.button_width, 
                    self.button_height, 
                    string='NO', 
                    name='cancel'
                )
            ),
            'okay': pygame.sprite.GroupSingle(
                Clickable(
                    left + self.button_width, 
                    bottom - offset,
                    self.button_width, 
                    self.button_height, 
                    string='YES', 
                    selected=True,
                    name='okay'
                )
            )
        }

        self.menu_items = MenuItems(items, selected_index=1)
        self.start_time = pygame.time.get_ticks()
        self.confirmed_time = None
    
    def confirm(self):
        self.confirmed_time = pygame.time.get_ticks()

        if self.args is not None:
            self.confirm_action(self.menu.args)
            self.has_confirmed = True
            return

        self.confirm_action()
        self.has_confirmed = True

    def popup(self):
        self.is_visible = True

    def close(self):
        """Reset everything when we close"""
        self.is_visible = False
        self.has_confirmed = False

    def render(self, game_surface):
        """Renders all the buttons on our escape menu"""
        self.surface.fill((255, 0, 0))

        if self.has_confirmed:
            elapsed = pygame.time.get_ticks() - self.confirmed_time
            rendered_text = self.font.render(self.text, False, colours.WHITE)
            self.surface.blit(rendered_text, (25,0))

            if elapsed >= 1000:
                self.close()

            return game_surface.blit(self.surface, (self.rect.centerx, self.rect.centery))

        rendered_text = self.font.render(self.prompt, False, colours.WHITE)
        self.surface.blit(rendered_text, (25, 0))
        self.menu_items.update()
        self.menu_items.items['cancel'].draw(self.surface)
        self.menu_items.items['cancel'].sprite.render()
        self.menu_items.items['okay'].draw(self.surface)
        self.menu_items.items['okay'].sprite.render()

        game_surface.blit(self.surface, (self.rect.centerx, self.rect.centery))
