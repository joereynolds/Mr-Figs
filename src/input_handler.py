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

    def handle_player_input(self,player, command):
        """Specialised function for dealing with a player's input"""
        directions = {'up':(0,-1),
                      'down':(0,1),
                      'left':(-1,0),
                      'right':(1,0),
                      'nothing':(0,0)}

        player.rect.x += directions[command][0] * player.speed
        player.rect.y += directions[command][1] * player.speed
        player.direction = command 

    def handle_input(self,player, level):
        pressed_keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            for k,v in InputHandler.keys.items():
                if pressed_keys[k]:
                    if v == 'reset':
                        level.reset()
                    elif v == 'next_level':
                        level.switch_to_scene(level.next_level)
                    else:
                        player.update(v)
                        for bomb in player.bombs: #Why is there collision code in our input handler???
                            bomb.bomb_collisions(player.bombs)
                        if v != 'space':#don't change state on the spikes when we plant a bomb
                            for sprite in level.sprites:
                                if isinstance(sprite ,tile.Spike):
                                    sprite.change_state()


 

