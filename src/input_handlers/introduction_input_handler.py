from src.event_command import EventCommand
import src.static_scenes

class IntroductionTextOverlayInputHandler():
    def __init__ (self, menu):
        self.menu = menu

    def process_input(self, event):
        if event['key'] == EventCommand.ACTION:
            if self.menu.text_index == len(self.menu.text) - 1:
                self.menu.user_data.register_has_seen_introduction()
                self.menu.switch_to_scene(src.static_scenes.level_obj_list['level-select'])
                return

            self.menu.text_index += 1
            # If we're past all of the indexes in our text box it'll throw an error.
            # Catch it and carry on to the actual game
