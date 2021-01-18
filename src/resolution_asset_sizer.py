import src.graphics as graphics
import src.logger as logger

class ResolutionAssetSizer():

    def __init__(self):
        self.available_resolutions = ((640, 480))

    def get_font_size(self, screen_size):
        return graphics.round_to_nearest_tile(screen_size[1] // graphics.tile_height)

    def get_button_height(self, screen_size):
        return graphics.round_to_nearest_tile(screen_size[1] // graphics.tile_height * 2)

    def get_button_offset(self, screen_size):
        return graphics.round_to_nearest_tile(screen_size[1] // graphics.tile_height * 2)

    def get_button_spacing(self, screen_size):
        return graphics.round_to_nearest_tile(screen_size[1] // graphics.tile_height * 2)

    def get_minimap_sprite_size(self, screen_size):

        default = {
            'sprite_placement_modifier': 3, 
            'width': graphics.tile_width * 3,
            'height': graphics.tile_height * 3,
        }

        return default
