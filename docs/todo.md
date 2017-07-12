# Todo
- Shake the screen when a bomb explodes
- Add a game over screen
- Add typehints where possible, this is painful
- Add __repr__'s for most things so debugging is easier and more useful
- Add a hotkey to display debugging info on the screen
- Add TODO annotations all over the code
- Center the level. At the moment the entire scene is in the top left corner.  This looks shit
- There's no way for the game to save your progress'
- Add WASD and HJKL controls
- Change the SCREEN variable in graphics.py to allow alpha transparency.
  This will allow us to 'overlay' other scenes onto one another i.e.
  having an escape menu and the level rendered behind it

#Bugs
- TODO Pressing 'X' only quits the game in the actual game, not the menus
- TODO Bombs don't kill you at the correct point. If you play level-2, When you walk down as your first move, that's meant to immediately kill you, but doesn't.
If you look at the blow_up() method that belongs to Bomb, it's very likely related to that
- TODO A bomb can destroy multiple blocks that are in a row. This should not work, it should be similar to Bomberman
- TODO Bombs shouldn't pass through solids
- TODO You can survive an explosion if you're standing on the bomb when it goes off. This is probably because no 'explosion particles' are hitting you . To fix this maybe check for collision against the bomb itself when it goes off? 
- TODO the trigger() function for Triggerable objects gets called 4 times perkeypress instead of once.
- TODO transparent surfaces dont work. For some reason, their transparency
  just slowly increases until they are opaque. See escape_menu_no_overlay.py foer an example, look in the render method.
