import src.graphics as graphics
import src.logger as logger

class ResolutionAssetSizer():

    def __init__(self):
        self.available_resolutions = ((640, 480))

    def get_nearest_available_resolution(self, screen_size):
        resolutions = [
            (640, 480),
            (768, 768),
            (1280, 960),
        ]

        if screen_size in resolutions:
            return screen_size

        for resolution in resolutions:
            if resolution[0] >= screen_size[0] and resolution[1] >= screen_size[1]:
                return resolution;

        logger.LOGGER.info('resolution not found in `available_resolutions` using scaling for 1280x960')
        return (1280, 960)

    def get_font_size(self, screen_size):
        return graphics.round_to_nearest_tile(screen_size[1] // graphics.tile_height // 3)

    def get_button_height(self, screen_size):
        return graphics.round_to_nearest_tile(screen_size[1] // graphics.tile_height * 1.5)

    def get_button_offset(self, screen_size):
        return graphics.round_to_nearest_tile(screen_size[1] // graphics.tile_height * 1.5)

    def get_button_spacing(self, screen_size):
        return graphics.round_to_nearest_tile(screen_size[1] // graphics.tile_height * 1.5)

    def get_minimap_sprite_size(self, screen_size):

        default = {
            'sprite_placement_modifier': 3, 
            'width': graphics.tile_width * 3,
            'height': graphics.tile_height * 3,
        }

        return default
