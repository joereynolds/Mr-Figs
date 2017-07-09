# Todo
- Add __repr__'s for most things so debugging is easier and more useful
- Add a hotkey to display debugging info on the screen
- Add TODO annotations all over the code
- Center the level. At the moment the entire scene is in the top left corner.
  This looks shit

#Bugs

- TODO Can't quit to main menu
- TODO Game starts at level 3 
- TODO level-select menu is linking to the wrong level (possible related to game starting at level 3) 
- TODO Bombs don't kill you at the correct point. If you play level-2, When you walk down as your first move, that's meant to immediately kill you, but doesn't.
If you look at the blow_up() method that belongs to Bomb, it's very likely related to that
- TODO A bomb can destroy multiple blocks that are in a row. This should not work, it should be similar to Bomberman
- TODO Bombs shouldn't pass through solids
- TODO You can survive an explosion if you're standing on the bomb when it goes off. This is probably because no 'explosion particles' are hitting you . To fix this maybe check for collision against the bomb itself when it goes off? 
- TODO the trigger() function for Triggerable objects gets called 4 times perkeypress instead of once.
