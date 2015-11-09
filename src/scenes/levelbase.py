import actor
import pygame
import colours
import graphics
import level_editor
import collision_handler 
import scenes.scenebase as scene_base
import scenes.escapemenu as escape_menu
import input_handlers.input_handler as input_handler
import input_handlers.global_input_handler as g_i_handler

class LevelBase(scene_base.SceneBase):

    def __init__(self,file,next_level):
        scene_base.SceneBase.__init__(self)
        self.file = file
        self.next_level = next_level
        self.level = level_editor.LevelData(file)
        self.level_tiles = self.level.data
        self.player = actor.Actor(
            48, 48,
            graphics.trans_width,
            graphics.trans_height,
            self.level,
            graphics.sprites['player']['sprites'][0]
        )
        self.sprites = pygame.sprite.LayeredUpdates()
        self.sprites.add(self.level_tiles, self.player)
        self.i_handler = input_handler.InputHandler(self.player, self.level, self)
        self.gi_handler = g_i_handler.GlobalInputHandler(
            self.player,
            self.i_handler
        )
        self.clock = pygame.time.Clock()
        self.escape_menu = escape_menu.EscapeMenu()

    def check_player_hasnt_died_a_horrible_death(self):
        """If the player has been destroyed, restart the level"""
        if not self.player in self.sprites:
            self.reset()

    def process_input(self):
        """Process the input for the level. Note that
        if the escape menu is open, we don't want to process input
        for the game itself but only for the escape menu.'"""
        if not self.escape_menu.is_open:
            self.gi_handler.process_input()
        self.escape_menu.process_input()

    def update(self):
        delta = self.clock.tick(60) / 1000.0
        self.player.update(delta)
        self.check_player_hasnt_died_a_horrible_death()
        self.sprites.add(self.player.bombs)
        self.sprites.move_to_front(self.player)
        for bomb in self.player.bombs:
            self.sprites.add(bomb.particles)

    def render(self):
        self.surface.fill(colours.WHITE)        
        self.sprites.draw(self.surface)

        if self.escape_menu.is_open:
            self.escape_menu.render()

        pygame.display.flip()

    def reset(self):
        """Reinitialises our level, kind of a hacky way
        of resetting the level again."""
        self.__init__(self.file, self.next_level)
