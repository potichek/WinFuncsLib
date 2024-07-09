import ctypes
import os

path_dll = str(ctypes.__path__[0])
path_dll = path_dll[0 : (len(path_dll) - 6)] + 'site-packages\\winfuncs\\WinFuncs.dll'
_WinFuncs_dll = ctypes.CDLL(path_dll)
_WinFuncs_dll.move_cursor_absolute.argtypes = (ctypes.c_short, ctypes.c_short)
_WinFuncs_dll.move_cursor.argtypes = (ctypes.c_short, ctypes.c_short)

def move_cursor(x: int, y: int) -> None:
    global _WinFuncs_dll
    _WinFuncs_dll.move_cursor(ctypes.c_short(x), ctypes.c_short(y))
    return

def move_cursor_absolute(x: int, y: int) -> None:
    global _WinFuncs_dll
    _WinFuncs_dll.move_cursor_absolute(ctypes.c_short(x), ctypes.c_short(y))
    return

def mouse_right_up() -> None:
    global _WinFuncs_dll
    _WinFuncs_dll.mouse_right_up()
    return

def mouse_right_down() -> None:
    global _WinFuncs_dll
    _WinFuncs_dll.mouse_right_down()
    return

def mouse_left_up() -> None:
    global _WinFuncs_dll
    _WinFuncs_dll.mouse_left_up()
    return

def mouse_left_down() -> None:
    global _WinFuncs_dll
    _WinFuncs_dll.mouse_left_down()
    return