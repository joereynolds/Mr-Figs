from src.event_command import EventCommand
import src.static_scenes

class InputHandler():
    def __init__ (self, game):
        self.game = game

    def process_input(self, event):
        if event['key'] == EventCommand.UP:
            self.game.player.direction = EventCommand.UP
        if event['key'] == EventCommand.DOWN:
            self.game.player.direction = EventCommand.DOWN
        if event['key'] == EventCommand.LEFT:
            self.game.player.direction = EventCommand.LEFT
        if event['key'] == EventCommand.RIGHT:
            self.game.player.direction = EventCommand.RIGHT
        if event['key'] == EventCommand.ACTION:
            crash_the_game()
