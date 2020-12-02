### Map Properties

`display_name` = This is the name of the map to display to the user. This is
optional, if you don't specify it, then the user is shown filepath. i.e.
`Walking`

`previous_level` = The path to the previous level (the one you just came from)
(this isn't used at the moment)

`next_level` = The path to the next level of the game i.e.  `./data/levels/tmx/my-cool-level.tmx`

`player_bomb_count` = The starting number of bombs for a player i.e. `1`

### Game Object Properties

`lifespan` = This is for bombs and it's how many turns a bomb will take until it
blows up. i.e. `5`

### Tile Types

For every tile in the object layer, we need to give it a `type` so that the game knows how to build that tile correctly.

Here's a list of the valid types

`actor` - This is the player

`bomb` - This is a normal bomb (not a pickup)

`destructible` - A destructible tile (usually a rock)

`tile` - Just a normal tile

`finish_tile` - The stairway

`portal` - A portal

`moveable_tile` - This is for boulders that can be pushed

`pickup_bomb` - The bomb pickup (the one with the yellow face)

`pressure_plate` - A pressure plate

`switch` - The switch

`triggerable` - The laser (bad name I know)

`video_tape` - The collectible video tape


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

#### Portals

`portal_id` = The id of the portal

`travels_to_portal_id` = The id of the portal that you want the user to travel
to


