from src.event_command import EventCommand
import src.static_scenes

class TextOverlayInputHandler():
    def __init__ (self, menu):
        self.menu = menu

    def process_input(self, event):
        if event['key'] == EventCommand.ACTION:
            self.menu.switch_to_scene(self.menu.redirect_to)
