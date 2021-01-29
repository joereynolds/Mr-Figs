from src.event_command import EventCommand
import src.static_scenes

class IntroductionTextOverlayInputHandler():
    def __init__ (self, menu):
        self.menu = menu

    def process_input(self, event):
        if event['key'] == EventCommand.ACTION:
            if self.menu.textbox.sprite.index == len(self.menu.textbox.sprite.text) - 1:
                self.menu.user_data.register_has_seen_introduction()
                self.menu.switch_to_scene(src.static_scenes.level_obj_list['level-select'])
                return

            self.menu.textbox.sprite.index += 1
