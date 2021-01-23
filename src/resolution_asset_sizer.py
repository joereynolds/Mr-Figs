import src.graphics as graphics
import src.logger as logger

class ResolutionAssetSizer():

    def get_font_size(self, screen_size):
        return int(self.get_button_size(screen_size)[0] * 0.25)

    def get_button_size(self, screen_size):
        """
        TODO - rename this method
        Gets the scaled up size of a tile in pixels
        """
        width_ratio = 16
        height_ratio = 9

        tile_width = screen_size[0] // width_ratio
        tile_height = screen_size[1] // height_ratio

        return tile_width, tile_height

    def get_minimap_sprite_size(self, screen_size):

        default = {
            'sprite_placement_modifier': 3, 
            'width': graphics.tile_width * 3,
            'height': graphics.tile_height * 3,
        }

        return default
