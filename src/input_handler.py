import event_handler
import pygame
import tile

class InputHandler():
    """Handles all input events. Key presses etc...
    Helps keep code clean...ish""" 

    keys = {pygame.K_UP:'up',
            pygame.K_DOWN:'down',
            pygame.K_LEFT:'left',
            pygame.K_RIGHT:'right',
            pygame.K_SPACE:'space',
            pygame.K_u:'u',
            pygame.K_r:'reset',
            pygame.K_l:'next_level',
            pygame.K_h:'previous_level'
            }

    def __init__(self):
        self.e_handler = event_handler.EventHandler()
        self.e_handler.add_event('laser_anim',27,2000)
        self.e_handler.add_event('bomb_anim',28,500)
        self.e_handler.handle_events() #est timers for all our events

    def handle_input(self,player, level):
        for event in pygame.event.get():
            if event.type == 27:
                for laser in level.level_tiles:
                    pass
            if event.type == 28:
                for bomb in player.bombs:
                    bomb.animate()
            
            if event.type == pygame.KEYDOWN:
                for k,v in InputHandler.keys.items():
                    if event.key == k:
                        if v == 'reset':
                            level.reset()
                        elif v == 'next_level':
                            level.switch_to_scene(level.next_level)
                        else: 
                            player.event_update(v)
                            for bomb in player.bombs: #Why is there collision code in our input handler???
                                bomb.bomb_collisions(player.bombs)
                            if v != 'space':#don't change state on the spikes when we plant a bomb
                                for sprite in level.level_tiles:
                                    if isinstance(sprite, tile.Stateful):
                                        sprite.update()
