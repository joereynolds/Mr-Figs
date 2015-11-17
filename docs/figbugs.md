#Bugs

- [ ] Can't quit to main menu
- [ ] Game starts at level 3 
- [ ] level-select menu is linking to the wrong level (possible related to game starting at level 3) 
- [ ] Bombs don't kill you at the correct point. If you play level-2, When you walk down as your first move, that's meant to immediately kill you, but doesn't.
If you look at the blow_up() method that belongs to Bomb, it's very likely related to that
- [ ] Hitting the stairs should advance you to the next level 
- [ ] A bomb can destroy multiple blocks that are in a row. This should not work, it should be similar to Bomberman
- [ ] Bombs shouldn't pass through solids
- [ ] You can survive an explosion if you're standing on the bomb when it goes off. This is probably because no 'explosion particles' are hitting you . To fix this maybe check for collision against the bomb itself when it goes off? 
- [ ] the trigger() function for Triggerable objects gets called 4 times perkeypress instead of once.







##Fixed bugs

- [x] The game should pause when we press 'esc'.
This was fixed by adding a state to GlobalInputHandler. If we're paused we 
execute a smaller portion of all input instead of the entire input from
the player. 

- [x] 'X' on the program window doesn't shut the application. 
Fixed by adding the correct event. if pygame.event == pygame.QUIT : pygame.quit()

- [x] Bombs should only update when I move. i.e. I can mash the arrows really quick and only move one tile but the bomb will have counted down multiple steps
Fixed by moving the update_bombs() call into the check for if our player is moving.
We only update the bombs if the player isn't moving (or has finished moving)  
