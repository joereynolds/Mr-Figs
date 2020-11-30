

class ResolutionAssetSizer():

    def __init__(self):
        self.available_resolutions = ((640, 480))

    def get_font_size(self, screen_size):
        font_size_map = {
            (640, 480): 18
        }


        return font_size_map.get(screen_size, 24)
