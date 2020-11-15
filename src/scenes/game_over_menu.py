import src.colours as colours
import src.scenes.scenebase as scene_base
import src.input_handlers.game_over_input_handler as input_handler

class GameOverMenu(scene_base.SceneBase):
    """Initial start menu at the start of the game"""

    def __init__(self):
        scene_base.SceneBase.__init__(
            self,
            input_handler.GameOverInput(self)
        )

    def render(self):
        """Fill our surface and render our buttons"""
        pass
