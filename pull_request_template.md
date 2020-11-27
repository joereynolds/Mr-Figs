# Regression testing

This is in place until we get some kind of automated testing done but it's a bit of a pain with games (or pygame at least).
Play through the game and confirm the following:

- [ ] - Bombs do not pass through solids
- [ ] - Once a moveable tile has been moved, bombs do not pass through it (or before it was moved)
- [ ] - A user stepping on a pressure plate activates the pressure plate
- [ ] - A user stepping off a pressure plate deactivates the pressure plate
- [ ] - The minimap is displaying properly
- [ ] - Moveable tiles cannot be pushed through solid
- [ ] - Explosions stop at stairs
- [ ] - Lasers kill you if you walk into them
- [ ] - A user walking into a solid tile while a bomb detonates will die
- [ ] - A user cannot walk into a moveable tile if that tile is up against a
  solid object
- [ ] - Explosion blow up destructible objects
