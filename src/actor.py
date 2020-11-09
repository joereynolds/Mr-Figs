import pygame

import src.bomb as bomb
import src.colours as colours
import src.entity as entity
import src.graphics as graphics
import src.movement_vector as movement_vector
import src.interpolate as interpolate
import src.collision_handler as collision_handler
import src.input_handlers.player_input_handler as p_i_handler

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

    @self.i_handler   = An InputHandler object

    @self.destination = [x,y] a 2 element list containing
                        the next destination the sprite will be travelling to

    @self.remaining_bombs = The number of bombs remaining in a level. This data is contained
                            in the tiled level data

    @self.valid_destinations = A list of valid moves that the user can make.
                               i.e. they can't move 13pixels if they themselves are 48px big.


    """
    def __init__(self, x, y, width, height, level, remaining_bombs, image=None):
        entity.Entity.__init__(self, x, y, width, height, image)

        self.remaining_bombs = int(remaining_bombs)
        self.direction = 'down'
        self.speed = 6
        self.distance = graphics.tile_width
        self.level = level
        self.tiled_level = self.level.tiled_level
        self.bombs = pygame.sprite.LayeredUpdates()
        self.move_stack = []
        self.destination = [self.rect.x, self.rect.y]
        self.valid_destinations = [graphics.tile_width * x for x in range(-100, 100)]
        self.moving = False
        self.input_handler = p_i_handler.PlayerInputHandler(self)
        self.collision_handler = collision_handler.PlayerCollisionHandler(
            self, self.level
        )

        self.minimap_colour = colours.BLUE_HIGHLIGHT

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
                self.tiled_level.get_tile_all_layers(target_x, target_y)
            ) :
            return

        else:
            if target_x < self.rect.x:
                self.rect.x -= self.speed
                self.moving = True
            elif target_x > self.rect.x:
                self.speed = interpolate.decelerate(self.rect.x, target_x)
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
        """Set's the next destination that our sprite is going to be
        moving/interpolating to"""
        if self.is_valid_move(x, y):
            self.destination[0] = self.rect.x + (x * self.distance)
            self.destination[1] = self.rect.y + (y * self.distance)

    def is_valid_move(self, x, y):
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

        if command in directions.keys():
            if not self.moving:
                self.set_destination(
                    directions[command][0],
                    directions[command][1]
                )
                self.set_direction(command)
                if command != 'space' :
                    self.update_bombs()
        if command == 'space':
            self.create_bomb()

    def update(self, delta_time):
        """These are actions that SHOULD be called every frame. Animation, collision checking etc..."""
        self.update_bomb_collection()
        self.move(delta_time)

    def create_bomb(self):
        """Creates a bomb underneath the players position"""
        if self.remaining_bombs:
            self.bombs.add(bomb.Bomb(
                self.rect.x,
                self.rect.y,
                graphics.tile_width,
                graphics.tile_height,
                self.tiled_level,
                5,
                graphics.sprites['bomb']['sprites'][0]
            ))
            self.remaining_bombs -= 1

    def is_dead(self):
        """Returns true if the player is dead"""
        return self not in self.level.sprites

    def animate_death(self):
        pass

    def update_bomb_collection(self):
        """Makes sure that not only do we process the bombs that we planted, but also
        the bombs that were already on the level"""
        for sprite in self.tiled_level.sprites:
            if isinstance(sprite, bomb.Bomb):
                self.bombs.add(sprite)

    def update_bombs(self):
        """Updates all bombs that are owned by the player.
        Usually, all bombs on the map are owned by the player,
        even the ones the player did not plant"""
        for bomb in self.bombs:
            bomb.lifespan -= 1
            if bomb.blow_up():
                self.bombs.remove(bomb)
