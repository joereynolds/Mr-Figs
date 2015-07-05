#Mr Figs ToDo

####GamePlay
- Spike sprites (read the spike section)
- Bomb blasts
- Fix undo functionality
- Need bomb sprite images
- Need player sprite images
- music
- Make the modules properly importable rather than having to copy and paste them into things
- Bomberman's starting position should be on the text file
- Create a backdrop for the game so that it's not just a horrible white background on smaller levels 
- Pressing 'r' should restart the level
- Need a main menu at the start
- Need a menu to display when you press 'esc'

###Code
- Hunt down all instances of subsurface that aren't in graphics.py and replace their hardcoded values with the variable defined in graphics.py



##Ideas

- Have a target amount of moves for each level. (i.e. let the user know it's possible to finish this level in 7 moves).

##Spike implementation

Spikes are an idea whereby every other move, the spikes will 'spike' up. If you are on the spike when it spikes up, you die and get reset to your original position.
If the spike is in the 'down' position, then you're safe :)

##Useful Links
[Bomberman mechanics](http://www.gamedev.net/page/resources/_/technical/game-programming/case-study-bomberman-mechanics-in-an-entity-component-system-r3159)