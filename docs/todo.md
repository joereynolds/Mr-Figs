#Bugs
- TODO A bomb can destroy multiple blocks that are in a row. This should not work, it should be similar to Bomberman
- TODO You can survive an explosion if you're standing on the bomb when it goes off. This is probably because no 'explosion particles' are hitting you . To fix this maybe check for collision against the bomb itself when it goes off? 
- TODO transparent surfaces dont work. For some reason, their transparency
  just slowly increases until they are opaque. See escape_menu_no_overlay.py foer an example, look in the render method.
