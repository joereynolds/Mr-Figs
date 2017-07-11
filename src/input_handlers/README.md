# Input Handlers

The purpose of extracting the input handlers is for modularity.
We increase redundancy but it also means some pretty good benefits like...

- 234442342534987456 players could all be playing with their own instance of an input handler
- Each scene can have entirely separate keybindings to the one before (and after!) it"
- It simplifies the classes that include the input handlers

The main reason of extracting them was for menu based navigation.
i.e

[R]esume Game
[Q]uit game
[L]evel select
etc...
