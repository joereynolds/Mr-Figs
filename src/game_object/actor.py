import pygame

from src.game_object.moveable_tile import MoveableTile
from src.game_object.triggerable import Triggerable
from src.game_object.bomb import Bomb
import src.colours as colours
import src.entity as entity
import src.graphics as g
import src.movement_vector as movement_vector
import src.interpolate as interpolate
from src.collision_handlers.turn_based_collision_handler import TurnBasedCollisionHandler

class Actor(entity.Entity):
    """
    @self.direction   = The last pressed direction.
                        When the sprite is still it will use this
                        to display the correct image for the sprite
                        depending on where they're facing.

    @self.speed       = The movement speed of the sprite from tile to tile

    @self.distance    = How far the Actor moves in one turn

    @self.tiled_level       = A level object. This contains
                        all tile information for that level and helps
                        make Actor aware of its surroundings.

    @self.bombs       = A list of Bomb objects planted by Actor

    @self.move_stack  = (not used) a stack of the previous moves of the actor

    @self.destination = [x,y] a 2 element list containing
                        the next destination the sprite will be travelling to

    @self.remaining_bombs = The number of bombs remaining in a level. This data is contained
                            in the tiled level data

    @self.valid_destinations = A list of valid moves that the user can make.
                               i.e. they can't move 13pixels if they themselves are 48px big.

    """
    def __init__(
            self, 
            x: int, 
            y: int, 
            width: int, 
            height: int, 
            level, 
            remaining_bombs: int, 
            image=None
        ):
        entity.Entity.__init__(self, x, y, width, height, image)

        self.remaining_bombs = int(remaining_bombs)
        self.direction = 'down'
        self.speed = 2
        self.distance = g.tile_width
        self.tiled_level = level

        self.image = g.spritesheet.subsurface(
                0 * g.tile_width, 
                12 * g.tile_height, 
                g.tile_width, 
                g.tile_height * 2
        ) 

        self.rect.y -= g.tile_height // 4

        # We don't want the character exactly on the tile, this doesn't look as good so
        # we offset the y position and then store that in here + our tiles height so we can
        # correctly check for tiles underneath us
        self.offset_y = (g.tile_height // 4) + g.tile_height # 40

        self.bombs = pygame.sprite.LayeredUpdates()
        self.move_stack = []
        self.destination = [self.rect.x, self.rect.y]
        self.valid_destinations = [g.tile_width * x for x in range(-100, 100)]
        self.moving = False # Whether or not we are moving
        self.is_teleporting = False # Whether or not we are being teleported by a portal
        self.creating_bomb = False  # Whether or not we are at this moment, creating a bomb
        self.minimap_colour = colours.BLUE_HIGHLIGHT

        self.animation_timer = 0.125
        self.frame_index = 0

        # True is Walking, false is idle
        self.frames = {
            'up': {
                True: [
                    g.spritesheet.subsurface(0 * g.tile_width, 34 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(1 * g.tile_width, 34 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(2 * g.tile_width, 34 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(3 * g.tile_width, 34 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(4 * g.tile_width, 34 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(5 * g.tile_width, 34 * g.tile_height, g.tile_width, g.tile_height * 2),
                ],
                False: [
                    g.spritesheet.subsurface(0 * g.tile_width, 16 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(1 * g.tile_width, 16 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(2 * g.tile_width, 16 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(3 * g.tile_width, 16 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(4 * g.tile_width, 16 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(5 * g.tile_width, 16 * g.tile_height, g.tile_width, g.tile_height * 2),
                ],
                'planting_bomb': [
                    g.spritesheet.subsurface(0 * g.tile_width, 22 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(1 * g.tile_width, 22 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(2 * g.tile_width, 22 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(3 * g.tile_width, 22 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(4 * g.tile_width, 22 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(5 * g.tile_width, 22 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(4 * g.tile_width, 22 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(3 * g.tile_width, 22 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(2 * g.tile_width, 22 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(1 * g.tile_width, 22 * g.tile_height, g.tile_width, g.tile_height * 2),
                ]
            },
            'down': {
                True: [
                    g.spritesheet.subsurface(0 * g.tile_width, 28 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(1 * g.tile_width, 28 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(2 * g.tile_width, 28 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(3 * g.tile_width, 28 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(4 * g.tile_width, 28 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(5 * g.tile_width, 28 * g.tile_height, g.tile_width, g.tile_height * 2),
                ],
                False: [
                    g.spritesheet.subsurface(0 * g.tile_width, 12 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(1 * g.tile_width, 12 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(2 * g.tile_width, 12 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(3 * g.tile_width, 12 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(4 * g.tile_width, 12 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(5 * g.tile_width, 12 * g.tile_height, g.tile_width, g.tile_height * 2),
                ],
                'planting_bomb': [
                    g.spritesheet.subsurface(0 * g.tile_width, 20 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(1 * g.tile_width, 20 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(2 * g.tile_width, 20 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(3 * g.tile_width, 20 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(4 * g.tile_width, 20 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(5 * g.tile_width, 20 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(4 * g.tile_width, 20 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(3 * g.tile_width, 20 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(2 * g.tile_width, 20 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(1 * g.tile_width, 20 * g.tile_height, g.tile_width, g.tile_height * 2),
                ]
            },
            'left': {
                True: [
                    g.spritesheet.subsurface(0 * g.tile_width, 32 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(1 * g.tile_width, 32 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(2 * g.tile_width, 32 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(3 * g.tile_width, 32 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(4 * g.tile_width, 32 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(5 * g.tile_width, 32 * g.tile_height, g.tile_width, g.tile_height * 2),
                ],
                False: [
                    g.spritesheet.subsurface(0 * g.tile_width, 18 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(1 * g.tile_width, 18 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(2 * g.tile_width, 18 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(3 * g.tile_width, 18 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(4 * g.tile_width, 18 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(5 * g.tile_width, 18 * g.tile_height, g.tile_width, g.tile_height * 2),
                ],
                'planting_bomb': [
                    g.spritesheet.subsurface(0 * g.tile_width, 26 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(1 * g.tile_width, 26 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(2 * g.tile_width, 26 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(3 * g.tile_width, 26 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(4 * g.tile_width, 26 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(5 * g.tile_width, 26 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(4 * g.tile_width, 26 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(3 * g.tile_width, 26 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(2 * g.tile_width, 26 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(1 * g.tile_width, 26 * g.tile_height, g.tile_width, g.tile_height * 2),
                ]
            },
            'right': {
                True: [
                    g.spritesheet.subsurface(0 * g.tile_width, 30 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(1 * g.tile_width, 30 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(2 * g.tile_width, 30 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(3 * g.tile_width, 30 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(4 * g.tile_width, 30 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(5 * g.tile_width, 30 * g.tile_height, g.tile_width, g.tile_height * 2),
                ],
                False: [
                    g.spritesheet.subsurface(0 * g.tile_width, 14 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(1 * g.tile_width, 14 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(2 * g.tile_width, 14 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(3 * g.tile_width, 14 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(4 * g.tile_width, 14 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(5 * g.tile_width, 14 * g.tile_height, g.tile_width, g.tile_height * 2),
                ],
                'planting_bomb': [
                    g.spritesheet.subsurface(0 * g.tile_width, 24 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(1 * g.tile_width, 24 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(2 * g.tile_width, 24 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(3 * g.tile_width, 24 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(4 * g.tile_width, 24 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(5 * g.tile_width, 24 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(4 * g.tile_width, 24 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(3 * g.tile_width, 24 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(2 * g.tile_width, 24 * g.tile_height, g.tile_width, g.tile_height * 2),
                    g.spritesheet.subsurface(1 * g.tile_width, 24 * g.tile_height, g.tile_width, g.tile_height * 2),
                ]
            },
        }

    def move(self, delta_time):
        """Checks to see if we've reached the destination given, if we have,
        we can stop moving. Note that we need to use delta-time otherwise we'll get
        differing results from pc to pc. Also without delta time we can't use fancy
        schmancy interpolation effects"""
        target_x = self.destination[0]
        target_y = self.destination[1]

        #Stop moving if the next tile we're going to is a solid
        if (self.rect.x == target_x and self.rect.y == target_y) \
            or self.tiled_level.find_solid_tile(
                self.tiled_level.get_tile_all_layers(target_x, target_y + self.offset_y)
            ) :
            return
        else:
            if target_x < self.rect.x:
                self.rect.x -= self.speed
                self.moving = True
            elif target_x > self.rect.x:
                # TODO - this interpolation breaks on the new tileset
                # definitely some maths error
                # self.speed = interpolate.decelerate(self.rect.x, target_x)
                self.rect.x += self.speed
                self.moving = True
            elif target_y < self.rect.y:
                self.rect.y -= interpolate.decelerate(self.rect.x, target_x)
                self.moving = True
            elif target_y > self.rect.y:
                self.rect.y += self.speed
                self.moving = True

        #If we have reached our destination, we're not moving anymore
        if self.rect.x == target_x and self.rect.y == target_y:
            self.moving = False

    def set_destination(self, x, y):
        """
        Set's the next destination that our sprite is going to be
        moving/interpolating to.

        This method name is a bit misleading, it doesn't take an x and a y.
        It takes a vector of 0 or 1 for both x and y.

        Passing something like player.set_destination(160, 320) will not set the
        destination to x:160 and y:320 but instead to x * 160 * 16 and y * 320 * 16
        AKA batshit nonsense.
        """
        if self.is_valid_move(x, y):
            self.destination[0] = self.rect.x + (x * self.distance)
            self.destination[1] = self.rect.y + (y * self.distance)

    def is_valid_move(self, x, y):
        # TODO - This calculation is identical to the one in set_destination
        # refactor it out
        player_wants_to_go_x = self.rect.x + (x * self.distance)
        player_wants_to_go_y = self.rect.y + (y * self.distance)

        tile = self.tiled_level.find_solid_tile(
            self.tiled_level.get_tile_all_layers(
                player_wants_to_go_x, player_wants_to_go_y
            )
        )

        if tile and not isinstance(tile, (MoveableTile, Triggerable)):
            return False

        return (x * self.distance) in self.valid_destinations \
            and (y * self.distance) in self.valid_destinations

    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction

    def add_bomb(self):
        self.remaining_bombs += 1

    def event_update(self, command):
        """These events should only happen on a keypress. They do not need to be checked
           every frame"""
        directions = movement_vector.vector
        self.tiled_level.sprites.change_layer(self, 1)

        if command in directions.keys():
            if not self.moving:
                self.set_destination(
                    directions[command][0],
                    directions[command][1]
                )
                self.set_direction(command)
                if command != 'action' :
                    self.update_bombs()
        if command == 'action':
            self.create_bomb()

    def update(self, delta_time=0):
        """These are actions that SHOULD be called every frame. Animation, collision checking etc..."""
        self.update_bomb_collection()
        self.move(delta_time)
        self.animate(delta_time)

    def create_bomb(self):
        """Creates a bomb underneath the players position"""
        if self.remaining_bombs and not self.moving:

            self.creating_bomb = True
            # Don't plant a bomb here if there's already one there
            for bomb in self.bombs:
                if bomb.rect.x == self.rect.x and bomb.rect.y == self.rect.y + self.offset_y:
                    return

            self.bombs.add(Bomb(
                self.rect.x,
                self.rect.y + self.offset_y,
                g.tile_width,
                g.tile_height,
                self.tiled_level,
                5,
                g.sprites['bomb']['sprites'][0]
            ))
            self.remaining_bombs -= 1

    def is_dead(self, dt):
        """Returns true if the player is dead"""
        if self not in self.tiled_level.sprites:
            self.animate_death(dt)
        return self not in self.tiled_level.sprites

    def animate(self, delta_time):
        self.animation_timer -= delta_time

        if self.animation_timer <= 0:

            if self.frame_index >= len(self.frames[self.direction][self.moving]) - 1:
                self.frame_index = 0

            self.frame_index += 1

            if self.creating_bomb:
                self.image = self.frames[self.direction]['planting_bomb'][self.frame_index]

            else: self.image = self.frames[self.direction][self.moving][self.frame_index]

            self.animation_timer = 0.125

            self.creating_bomb = False

    def animate_death(self, dt):
        print('death animation here')

    def update_bomb_collection(self):
        """Makes sure that not only do we process the bombs that we planted, but also
        the bombs that were already on the level"""
        for sprite in self.tiled_level.sprites:
            if isinstance(sprite, Bomb):
                self.bombs.add(sprite)

    def update_bombs(self):
        """Updates all bombs that are owned by the player.
        Usually, all bombs on the map are owned by the player,
        even the ones the player did not plant"""
        
        for bomb in self.bombs:
            # Don't decreate the lifespan of a bomb if we're going to it.
            # This would cause it to blow up even if we've collected it.
            if self.destination[0] != bomb.rect.x or self.destination[1] != bomb.rect.y:
                bomb.lifespan -= 1
                if bomb.blow_up():
                    self.bombs.remove(bomb)
