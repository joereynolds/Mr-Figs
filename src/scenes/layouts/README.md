
# XML Format

## Component

### X

The x co-ordinate of the component

### Y 

The y co-ordinate of the component

### Width

The width of the component

### Height

The height of the component

### Type

The class of the component 

### Name

A human readable name that is later referenceable
i.e. 

With this XML
```
<component x='350' y='100' width='100' height='50' type="gui_base.Clickable" name="start-game">
    <text>START GAME</text>
</component>
```

you can do this
```
component_dict['start-game'].on_click
```
