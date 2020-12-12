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
        font_size_map = {
            (640, 480): 18
        }

        return font_size_map.get(screen_size, 24)

    def get_button_offset(self, screen_size):
        button_offset_map = {
            (640, 480): 64
        }
        return button_offset_map.get(screen_size, 256)

    def get_button_spacing(self, screen_size):
        button_spacing_map = {
            (640, 480): 32
        }
        return button_spacing_map.get(screen_size, 64)

    def get_minimap_sprite_size(self, screen_size):
        minimap_sprite_size_map = {
            (640, 480): {
                'sprite_placement_modifier': 0.5, 
                'width': graphics.tile_width // 2,
                'height': graphics.tile_height // 2,
            },
            (768, 600): {
                'sprite_placement_modifier': 0.5, 
                'width': graphics.tile_width // 2,
                'height': graphics.tile_height // 2,
            },
            (768, 768): {
                'sprite_placement_modifier': 0.5, 
                'width': graphics.tile_width // 2,
                'height': graphics.tile_height // 2,
            }
        }

        default = {
            'sprite_placement_modifier': 1, 
            'width': graphics.tile_width,
            'height': graphics.tile_height,
        }

        return minimap_sprite_size_map.get(screen_size, default)
