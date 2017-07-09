# Mr-Figs
Mr Figs is a turn-based puzzler in the style of good ol' Bomberman.
The player must blast their way through various puzzles to reach the end goal.

mr-figs runs on python 3.x

#### Demo (WIP)

![alt text](figDemo.gif)

#### Installation
```
git clone https://github.com/joereynolds/Mr-Figs
cd mr-figs
python3 install.py
```

You can then play mr-figs by navigating into ```src``` and running ```run.py```

##### Installation Failed :(

If for any reason the install script failed, These are the dependencies to install manually.

- Wheel 
    - Allows the building of wheel files
- Pygame
    - Mr Figs uses the Pygame library for pretty much everything!
- [PyTMX](https://github.com/bitcraft/PyTMX)
    - The parser for .tmx files

#### Other libraries
These are already included/not needed but I thought I'd include them just to cover all grounds.

- [Tiled](https://github.com/bjorn/tiled)
    - Mr Figs uses Tiled for all level editing. This helps cut down on boilerplate in the code. In order to parse Tiled's format, I'm using... 

#### Write-ups
['Undo' Functionality](http://joereynoldsaudio.com/programming/Articles/undo-in-pygame)

[Building a Level Editor](http://joereynoldsaudio.com/programming/Articles/building-a-level-editor)

#### Contributing

Any contributions are welcome but ideally, grep for 'TODO'
in the codebase and do one of those :D
