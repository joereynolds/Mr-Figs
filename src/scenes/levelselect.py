import pygame
import gui_base
import graphics
import environment
import scenes.scenebase as scene_base

class LevelMenu(scene_base.SceneBase):

    def __init__(self):
        scene_base.SceneBase.__init__(self)
        self.level_container = gui_base.LevelSelectContainer(90,90,90,90)
        self.buttons = pygame.sprite.Group()
        self.components = self.level_container.components
        self.buttons.add(self.level_container.components)
        self.game_levels = environment.create_level_list()

    def update(self):
        for event in pygame.event.get():
            for i, level in enumerate(self.level_container.components):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    level.on_click(
                        self.switch_to_scene, 
                        self.game_levels[i]
                    )

    def render(self):
        """Renders a button for each level that is in the game"""
        self.surface.fill((255,255,255))
        self.buttons.draw(self.surface)
        pygame.display.flip()


