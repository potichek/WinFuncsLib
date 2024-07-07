from ._winfuncs import *

def move_cursor(x, y):
    _winfuncs.move_cursor(x, y)
    return

def move_cursor_absolute(x, y):
    _winfuncs.move_cursor_absolute(x, y)
    return

def mouse_right_up():
    _winfuncs.mouse_right_up()
    return

def mouse_right_down():
    _winfuncs.mouse_right_down()
    return

def mouse_left_up():
    _winfuncs.mouse_left_up()
    return

def mouse_left_down():
    _winfuncs.mouse_left_down()
    return