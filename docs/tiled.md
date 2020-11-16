### Map Properties

`display_name` = This is the name of the map to display to the user. This is
optional, if you don't specify it, then the user is shown filepath

`previous_level` = The path to the previous level (the one you just came from)

`next_level` = The path to the next level of the game

`player_bomb_count` = The starting number of bombs for a player

`player_starting_x` = The *grid* coordinates of the player's starting x position.
Default is 1 you don't need to specify this

`player_starting_y` = The *grid* coordinates of the player's starting y position.
Default is 1 you don't need to specify this


### Game Object Properties

`lifespan` = This is for bombs and it's how many turns a bomb will take until it
blows up

`destructable` = Whether or not a tile can be destroyed by a bomb

`moveable` = Whether or not a tile can be moved by the player

`solid` = Whether or not the player can walk through it

#### Portals

`portal_id` = The id of the portal

`travels_to_portal_id` = The id of the portal that you want the user to travel
to
