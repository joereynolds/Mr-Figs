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
- Need a main menu at the start
- Need a menu to display when you press 'esc'

###Code
- Hunt down all instances of subsurface that aren't in graphics.py and replace their hardcoded values with the variable defined in graphics.py
- Package it into an exe
- Debug options such as '<' to go back a level, and '>' to go forward a level



##Ideas

- Have a target amount of moves for each level. (i.e. let the user know it's possible to finish this level in 7 moves).

##Spike implementation

Spikes are an idea whereby every other move, the spikes will 'spike' up. If you are on the spike when it spikes up, you die and get reset to your original position.
If the spike is in the 'down' position, then you're safe :)

There are 3 options of how bombs can be implemented. 

1. Bombs can be planted on the spike as long as the spike is down. When the spike comes up, it will detonate the bomb.
2. Bombs cannot be planted on spikes.
3. Bombs can be planted on spikes regardless of position.

##Useful Links
[Bomberman mechanics](http://www.gamedev.net/page/resources/_/technical/game-programming/case-study-bomberman-mechanics-in-an-entity-component-system-r3159)
