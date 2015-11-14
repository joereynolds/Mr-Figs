#Bugs

- [] Can't quit to main menu
- [] Game starts at level 3 
- [] level-select menu is linking to the wrong level (possible related to game starting at level 3) 
- [] Bombs don't kill you at the correct point. If you play level-2, When you walk down as your first move, that's meant to immediately kill you, but doesn't. 
- [] Hitting the stairs should advance you to the next level 
- [] Bombs should only update when I move. i.e. I can mash the arrows really quick and only move one tile but the bomb will have counted down multiple steps
- [] A bomb can destroy multiple blocks that are in a row. This should not work, it should be similar to Bomberman
- [] Bombs shouldn't pass through solids
- [] The game should pause when we press 'esc'
- [] You can survive an explosion if you're standing on the bomb when it goes off. This is probably because no 'explosion particles' are hitting you . To fix this maybe check for collision against the bomb itself when it goes off? 
- [] the trigger() function for Triggerable objects gets called 4 times perkeypress instead of once.







##Fixed bugs
- [x] 'X' on the program window doesn't shut the application. 
Fixed by adding the correct event. if pygame.event == pygame.QUIT : pygame.quit()
