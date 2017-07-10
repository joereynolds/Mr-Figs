import pygame
import event_handler
import collision_handler
import input_handlers.input_handler as input_handler


class GlobalInputHandler():
    """Takes all other input handler, and encapsulates them
    so that we don't get any conflicts between key presses and
    we keep code clean"""

    #TODO instantiation here could be simpler, I think
    #level_base is already contained inside level
    def __init__(self, player, level, level_base):
        """
        
        """
        self.level = level
        self.level_base = level_base
        self.player = player
        self.player_input_handler = player.input_handler
        self.level_input_handler = input_handler.InputHandler(
            self.player,
            self.level,
            self.level_base
        )
        self.e_handler = event_handler.EventHandler(player)

    def process_input(self):
        """Processes input for everything. Note that
        in certain cases we are only processing input if a key has
        been pressed. No need to process something unless needed"""

        if self.level_base.escape_menu.is_menu_open():
            for event in pygame.event.get():
                self.level_base.escape_menu.process_input(event)
                if event.type == pygame.KEYDOWN:
                    self.level_input_handler.process_input(event)
        else:
            for event in pygame.event.get():
                self.e_handler.handle_events(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                elif event.type == pygame.KEYDOWN:
                    self.player_input_handler.process_input(event)
                    self.level_input_handler.process_input(event)
