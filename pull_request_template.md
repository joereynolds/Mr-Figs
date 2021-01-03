# Regression testing

This is in place until we get some kind of automated testing done but it's a bit of a pain with games (or pygame at least).
Play through the game and confirm the following:

### Bombs
- [ ] - Bombs do not pass through solids
- [ ] - Explosions stop at stairs
- [ ] - A user walking into a solid tile while a bomb detonates will die
- [ ] - Explosion blow up destructible objects
- [ ] - Bombs do not blow up things when collected at 1

### Moveable tiles
- [ ] - Once a moveable tile has been moved, bombs do not pass through it (or before it was moved)
- [ ] - Moveable tiles cannot be pushed through solid
- [ ] - A user cannot walk into a moveable tile if that tile is up against a solid object

### Pressure plates
- [ ] - A user stepping on a pressure plate activates the pressure plate
- [ ] - A user stepping off a pressure plate deactivates the pressure plate

### Lasers
- [ ] - Lasers kill you if you walk into them

### Minimap
- [ ] - The minimap is displaying properly

### Other
- [ ] - Tiles can have other tiles beneath them
