### Mechanics

- The game is turn based, when the player moves that is considered a 'turn'

- The level is completed when the player reaches the staircase

- Each level has a predefined amount of bombs that the player begins with (ranging from 0 and upwards)

- The player can plant bombs which will destroy destructible terrain and activate switches

- A tile can be
    - destructible (can be blown up by a bomb)
    - solid (a player can't go through it)
    - moveable (a player can push it)

### In-game objects

- Player - The player. Put him where you want on the map

- Bomb - Pretty self explanatory. When a player plants a bomb, it starts
  counting from 5 meaning the player can make 5 turns and then it explodes.
  Bomb's can also be picked up. As an example if you plant a bomb and realise
  you've made a mistake, you can walk into it to collect it again.  There are
  also 'unactivated' bombs which can be picked up too (these have a yellowish
  cover).  A bomb's radius is 3 tiles from the bomb (shown below)


```
B = bomb
x = part of explosion
. = ground

...x...
...x...
...x...
xxxBxxx
...x...
...x...
...x...
```

- Rocks - Just a solid tile that can be destroyed by a bomb

- Boulders - These are pushable rocks. When the player moves into it, it will
  also move

- Pressure Plate - This will (de)activate a laser when something is on top of it

- Switch - This will (de)activate a laser when it's been turned on (by blowing
  it up with a bomb)

- Laser - This is a tile that will kill you if you come in contact with it

- Portals - These are two way and transfer the player to and from each portal

### Map Size

The map size can be as big or small as you want (just don't do something
ridiculous like 60000x60000 tiles). The camera scrolls to accommodate large
levels. Whatever works and plays well is always preferred.

### Software

For the smoothest experience I *highly* recommend downloading [tiled map
editor](https://www.mapeditor.org/download.html). Then you can just copy and
paste a pre-existing level and adjust it to your needs.

### Workflow

- Clone or download this repository
- make a copy of a level (`tutorial-pressure-plates.tmx` is a good one)
- Open up tiled and open your newly created file
- Edit to your hearts content
- Send it over

### Delivered product

If you can, a complete level with all the relevant properties added to tiles in
the editor is the way to go.

I understand if you don't/can't do this. In those cases, just a jpeg of the
layout is fine and I'll convert it over.
