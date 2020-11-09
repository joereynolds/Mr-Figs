# Mr-Figs

Mr Figs is a turn-based puzzler in the style of good ol' Bomberman.
The player must blast their way through various puzzles to reach the end goal.

Mr-Figs runs on python 3.x

#### Demo (WIP)

![alt text](figDemo.gif)

#### Gameplay

- Plant bombs with `<space>`
- Move with either `WASD`, `HJKL` or the arrow keys
- Pickup bombs to add to your inventory
- Pickup previously planted bombs if you made a mistake
- Make your way to the stairs

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
