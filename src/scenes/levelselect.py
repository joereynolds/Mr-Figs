import src.colours as colours
import src.scenes.scenebase as scene_base
import src.input_handlers.level_select_input_handler as input_handler

class LevelMenu(scene_base.SceneBase):

    def __init__(self, levels):
        """
        @levels A dict of our levels that comes from environment.create_level_list
        """
        scene_base.SceneBase.__init__(
            self,
            input_handler.LevelSelectInput(
                self
            )
        )

        self.game_levels = levels

    def render(self):
        """Renders a button for each level that is in the game"""
        pass
