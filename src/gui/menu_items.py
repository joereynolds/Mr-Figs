import pygame


class MenuItems():

    def __init__(self, menu_items, selected_index=0):
        self.items = menu_items
        self.menu_item_map = list(self.items.keys())
        self.selected_index = selected_index
        self.last_mouse_pos = (0,0)

    def get_selected_item(self):
        return self.items[self.menu_item_map[self.selected_index]].sprite
    
    def update(self):
        """Checks for mouse collisions in all our items"""
        mouse_pos = pygame.mouse.get_pos()
        for item in self.menu_item_map:
            if self.last_mouse_pos != mouse_pos and self.items[item].sprite.rect.collidepoint(mouse_pos):
                self.select_item_by_name(item)
                self.last_mouse_pos = mouse_pos

    def select_item_by_name(self, name: str):
        """'selects' the sprite by name. This is useful for the mouse to
        select the button under the cursor."""

        # unselect everything before we select our item
        for item in self.items:
            self.items[item].sprite.selected = False

        self.items[name].sprite.selected = True
        self.selected_index = self.menu_item_map.index(name)

    def select_previous_item(self):
        self.items[self.menu_item_map[self.selected_index]].sprite.selected = False

        # TODO - can probably clean this up with modulo
        self.selected_index -= 1
        if self.selected_index < 0:
            self.selected_index = len(self.menu_item_map) - 1

        self.items[self.menu_item_map[self.selected_index]].sprite.selected = True

    def select_next_item(self):
        self.items[self.menu_item_map[self.selected_index]].sprite.selected = False

        # TODO - can probably clean this up with modulo
        self.selected_index += 1
        if self.selected_index >= len(self.menu_item_map):
            self.selected_index = 0

        self.items[self.menu_item_map[self.selected_index]].sprite.selected = True

