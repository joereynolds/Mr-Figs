import src.entity as entity
import src.environment
import src.colours as colours
from src.game_object.light_source import LightSource

class Torch(entity.Entity):
    def __init__(self, x, y, width, height, level, image=None):
        entity.Entity.__init__(self, x, y, width, height, image)
        translated = level.map_layer_for_camera.translate_rect(self.rect)

        self.light_mask = LightSource(
            translated.x + 128, 
            translated.y, 
            width, 
            height
        )

