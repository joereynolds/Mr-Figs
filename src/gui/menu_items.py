class MenuItems():

    def __init__(self, menu_items, selected_index=0):
        self.items = menu_items
        self.menu_item_map = list(self.items.keys())
        self.selected_index = selected_index

    def get_selected_item(self):
        return self.items[self.menu_item_map[self.selected_index]].sprite

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

