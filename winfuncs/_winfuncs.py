import ctypes
import os

home_path = str(ctypes.__path__[0])
home_path = home_path[0: (len(home_path) - 6)] + 'site-packages\\winfuncs\\'
_WinFuncs_dll = ctypes.CDLL(home_path + 'WinFuncs.dll');
_WinFuncs_dll.move_cursor_absolute.argtypes = (ctypes.c_short, ctypes.c_short)
_WinFuncs_dll.move_cursor.argtypes = (ctypes.c_short, ctypes.c_short)
_WinFuncs_dll.set_dll_directory.argtypes = (ctypes.c_wchar_p, )
_WinFuncs_dll.set_dll_directory(ctypes.c_wchar_p(home_path))

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

def turnoff_keyboard() -> None:
    global _WinFuncs_dll
    _WinFuncs_dll.turnoff_keyboard()
    return

def turnon_keyboard() -> None:
    global _WinFuncs_dll
    _WinFuncs_dll.turnon_keyboard()
    return

def turnoff_monitor() -> None:
    global _WinFuncs_dll
    _WinFuncs_dll.turnoff_monitor()
    return

def turnon_monitor() -> None:
    global _WinFuncs_dll
    _WinFuncs_dll.turnon_monitor()
    return
