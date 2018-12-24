import colours
import container_reader
import scenes.scenebase as scene_base
import input_handlers.game_over_input_handler as input_handler

class GameOverMenu(scene_base.SceneBase):
    """Initial start menu at the start of the game"""

    def __init__(self):
        scene_base.SceneBase.__init__(
            self,
            input_handler.GameOverInput(self)
        )
        self.reader = container_reader.ContainerReader('game_over.xml')
        self.component_dict = self.reader.component_dict
        self.components = self.reader.components

    def render(self):
        """Fill our surface and render our buttons"""
        self.surface.fill(colours.WHITE)
        self.components.draw(self.surface)
        for component in self.components:
            component.render_text()
