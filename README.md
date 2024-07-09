# WinFuncs Library #
## What is this? ##
Simplifying various WinAPI functions, with this library you won`t need to use ctypes to call WinAPI functions.

## Working with the library ##

**move_cursor_absolute(x: int, y: int) -> None**
moves the cursor to the specified coordinates.
arguments:
```x: int``` - координата x.
```y: int``` - координата y.
returns: None.
Note: The x and y values must be at least 0 and no more than 65535.

Example:
```python
winfuncs.move_cursor_absolute(0,0)
# The cursor moves to the upper left corner
```

**move_cursor(x: int, y: int) -> None**
moves the cursor to the specified coordinates relative to the current cursor position.
arguments:
```x: int``` - координата x.
```y: int``` - координата y.
returns: None.
Note: x and y are the number of pixels that the cursor will be moved to.

Example:
```python
winfuncs.move_cursor(0, 100)
# The cursor moves 100 pixels along the y axis
```

**mouse_right_up() -> None**
Simulates releasing the right mouse button.
arguments: nothing
returns: None.
Note: nothing.

Example:
```python
winfuncs.mouse_right_up()
```

**mouse_right_down() -> None**
Simulates right-click.
arguments: nothing
returns: None.
Note: nothing.

Example:
```python
winfuncs.mouse_right_down()
```

**mouse_left_down() -> None**
Simulates left-click.
arguments: nothing
returns: None.
Note: nothing.

Example:
```python
winfuncs.mouse_left_down()
```

**mouse_left_up() -> None**
Simulates raising the left mouse button.
arguments: nothing
returns: None.
Note: nothing.

Example:
```python
winfuncs.mouse_left_up()
```