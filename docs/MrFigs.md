#Mr Figs ToDo


###General
- Need a menu to display when you press 'esc'

###Imagery

- Spike sprites (read the spike section)
- Bomb blasts
- Need bomb sprite images
- Need player sprite images
- Create a backdrop for the game so that it's not just a horrible white background on smaller levels

###Music & SFX

As there are 5 areas to Mr Figs (Grass, Desert/Beach, Cave, Snow, Castle),
There will need to be a **minimum** of 5 tracks (1 per area).

Ideally the music will be the same track but maybe with different themes going on? Look up 'Stiglitz' as an example. The verses are happy but the chorus is evil. Perhaps we could have have for the Desert and then evil for Cave. Or something along those lines...


#####Music

- Grass Track
- Desert Track
- Snow Track
- Cave Track
- Castle Track

#####SFX

There will need to be sound effects for the following sounds

- Bomb placement 
	-  Ideally 2-3 variations of the placement

- Bomb explosion
	- Again, 2-3 different variations of the explosion

- Spikes

- Ambience
	- Ambience for each level
		- Wind for the desert level
		- Birds/tweets for grass etc...


###Code

- Package it into an exe
- Make the modules properly importable rather than having to copy and paste them into things
- Bomberman's starting position should be on the text file
- Fix undo functionality

##Ideas

- Have a target amount of moves for each level. (i.e. let the user know it's possible to finish this level in 7 moves).

##Spike implementation

Spikes are an idea whereby every other move, the spikes will 'spike' up. If you are on the spike when it spikes up, you die and get reset to your original position.
If the spike is in the 'down' position, then you're safe :)

There are 3 options of how bombs can be implemented. 

1. Bombs can be planted on the spike as long as the spike is down. When the spike comes up, it will detonate the bomb.
2. Bombs cannot be planted on spikes.
3. ~~Bombs can be planted on spikes regardless of position.~~

##Useful Links
[Bomberman mechanics](http://www.gamedev.net/page/resources/_/technical/game-programming/case-study-bomberman-mechanics-in-an-entity-component-system-r3159)
