<img src="./assets/images/mr-figs-title-draft.png" alt="Mr Figs" width="100%">


Mr Figs is a turn-based puzzler.
The player must blast their way through various puzzles to reach the end goal.

## NOTE TO PLAYERS

This game uses proprietary assets. You can checkout this commit
`b3e6a30a82526117682d54d2e583d6d844607181` and the game will use public domain
assets (the ones featured in the gifs) (though its also missing out on lots of
updates).

The future of this game is based off of proprietary assets.  I hope to one day in the
future make it compatible with the free assets again but for now, consider this
repository a showcase of the game rather than something you can clone down and
play (unless you want to run `git checkout b3e6a30a82526117682d54d2e583d6d844607181` and play the demo version).

#### Demo Gif

![](https://github.com/joereynolds/Mr-Figs/blob/master/figs.gif)

#### Gameplay

- Plant bombs with `<space>`
- Move with either `WASD`, `HJKL` or the arrow keys
- Pickup bombs to add to your inventory
- Pickup previously planted bombs if you made a mistake
- Try and find all the hidden video tapes to reveal the story behind Mr Figs and the lab
- Activate switches by blowing them up
- Trigger pressure plates by putting something on them
- Teleport around by going through portals
- Watch out for patrolling bad guys
- Make your way to the stairs
- PS4 controller support (tested on Ubuntu)
- Xbox 360 controller support (tested on Ubuntu)

#### Storyline

Mr-Figs is the result of an experiment gone wrong. For years he's been studying
the patterns of the mad scientist behind all of this in a plan to escape and
expose the experiments that have been going on within the walls of the
laboratory that he was raised in.

Tonight is the night he has planned for all this time.


#### Installing

```
make install
```

Then

```
./run.py
```

##### Troubleshooting

See the [troubleshooting doc](./docs/troubleshooting.md)

#### Write-ups

['Undo' Functionality](https://joereynoldsaudio.com/2018/06/12/undo-in-pygame.html)

#### Contributing

Any contributions are welcome but ideally, grep for 'TODO'
in the codebase and do one of those :D

#### Running the tests

```
python3 -m unittest discover -v
```

#### Directory structure

```
├── build (Build scripts)
├── data (Game data e.g. images, audio)
├── docs (Extra documentation)
├── levels (Level data)
├── src (source code)
└── test (tests live here)
```

### Level design

If you are designing levels for mr-figs please read the [level-design
doc](./docs/level-design.md)
