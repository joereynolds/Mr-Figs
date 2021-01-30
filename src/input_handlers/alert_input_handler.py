import src.static_scenes
import pygame
from src.event_command import EventCommand


class AlertInput():

    def __init__(self, menu):
        self.menu = menu

    def process_input(self, event):
        if event['key'] in EventCommand.LEFT:
            self.menu.menu_items.select_next_item()
        if event['key'] == EventCommand.RIGHT:
            self.menu.menu_items.select_previous_item()
        if event['key'] == EventCommand.ACTION:
            item = self.menu.menu_items.get_selected_item()

            if item.name == 'cancel':
                self.menu.close()
            
            if item.name == 'okay':
                self.menu.confirm()
