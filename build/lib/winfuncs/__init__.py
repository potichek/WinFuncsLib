from ._winfuncs import *

def move_cursor(x, y) -> None:
    _winfuncs.move_cursor(x, y)
    return

def move_cursor_absolute(x, y) -> None:
    _winfuncs.move_cursor_absolute(x, y)
    return

def mouse_right_up() -> None:
    _winfuncs.mouse_right_up()
    return

def mouse_right_down() -> None:
    _winfuncs.mouse_right_down()
    return

def mouse_left_up() -> None:
    _winfuncs.mouse_left_up()
    return

def mouse_left_down() -> None:
    _winfuncs.mouse_left_down()
    return

def turnoff_keyboard() -> None:
    _winfuncs.turnoff_keyboard()
    return

def turnon_keyboard() -> None:
    _winfuncs.turnon_keyboard()
    return

def turnoff_monitor() -> None:
    _winfuncs.turnoff_monitor()
    return

def turnon_monitor() -> None:
    _winfuncs.turnon_monitor()
    return
