### Map Properties

`display_name` = This is the name of the map to display to the user. This is
optional, if you don't specify it, then the user is shown filepath. i.e.
`Walking`

`previous_level` = The path to the previous level (the one you just came from)
(this isn't used at the moment)

`next_level` = The path to the next level of the game i.e.  `./data/levels/tmx/my-cool-level.tmx`

`player_bomb_count` = The starting number of bombs for a player i.e. `1`

`has_video_tape` = If the level has a video tape, set this so the level is aware of it


### Tile Types

For every tile in the object layer, we need to give it a `type` so that the game knows how to build that tile correctly.

Here's a list of the valid types and their properties (if any)

#### actor

This is the player

#### barrel/barrel_up/barrel_down/barrel_left/barrel_right/barrel_up_left/barrel_up_right/barrel_down_left/barrel_down_right

These fire bullet out of them at a certain rate.

Each different type (left, up, down etc...) corresponds to the direction for the bullet to go in.

`pattern` - The pattern to fire bullets in, can be either `constant` (fire at the same rate) or `burst` (fire in bursts of 3 before cooling down again)

#### bomb

This is what the player can drop

`lifespan` = This is for bombs and it's how many turns a bomb will take until it
blows up. i.e. `5`

#### destructible   

A destructible tile (usually a rock) is a tile that can be destroyed by a bomb

`tile` - Just a normal tile

#### enemy_bombable

This is an enemy that follows a predetermined path and also plants bombs at random opportunities.

`follows_path_id` - The id of the path to follow (path must be in the "paths" layer)

#### enemy_pathable

This is an enemy that follows a predetermined path

`follows_path_id` - The id of the path to follow (path must be in the "paths" layer)

#### path

This is a path that is followed by various other in game objects (enemy_pathable, enemy_bombable, platform etc...)

`path_id` - The id of the path

#### platform

When the player collides with this they are taken on a journey on top of the platform.
It uses the `path` for its path.

`follows_path_id` - The id of the path to follow (path must be in the "paths" layer)

#### portal

This teleports the user to another portal when the user collides with it.
In order for teleportation to work we must link the tiles with an id and a destination portals id.

`portal_id` = The id of the portal

`travels_to_portal_id` = The id of the portal that you want the user to travel
to

#### moveable_tile

This is a tile that can be pushed (almost always a boulder)

#### pickup_bomb

This is an undetonated bomb that can be picked up by the player

#### pressure_plate

A pressure plate

#### scene_switching_tile

This is usually the staircase. When the player collides with it,
they are taken to a specified scene.

`scene` - A filepath of the next scene (.tmx file) to go to

#### switch

The switch

#### triggerable
The laser (bad name I know)

#### video_tape

This is what the player must collect to reveal the full story of the experiments

`story` - A filepath to a file containing text.


#### Linking lasers, switches and pressure plates

A switch/pressure_plate has this property

`triggers`

Then give the same number to the laser you want to activate with this name

`triggered_id`

So, if we have a switch we want to hook to a laser we'd have:

```
switch:triggers=1
triggerable:triggered_id=1
```
