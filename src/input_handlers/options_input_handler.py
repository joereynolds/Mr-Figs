import src.static_scenes
from src.user_data import UserData
from src.event_command import EventCommand
from src.gui.alert import Alert


class OptionsInputHandler():
    """Handles input for the options menu"""

    def __init__(self, menu):
        self.menu = menu
        self.save = UserData()

    def process_input(self, event):
        if self.menu.confirm_delete_save_alert.is_visible:
            return self.menu.confirm_delete_save_alert.input_handler.process_input(event)

        if event['key'] == EventCommand.DOWN:
            self.menu.menu_items.select_next_item()
        if event['key'] == EventCommand.UP:
            self.menu.menu_items.select_previous_item()
        if event['key'] == EventCommand.ACTION:
            item = self.menu.menu_items.get_selected_item()

            if item.name == 'clear_data':
                self.menu.confirm_delete_save_alert.popup()
                self.save.delete_save_data()
        
            if item.name == 'toggle_music':
                self.menu.menu_items.items['toggle_music'].sprite.toggle(
                    self.save.toggle_music_option
                )

            if item.name == 'go_back':
                self.menu.switch_to_scene(src.static_scenes.level_obj_list['start-menu'])
