import ctypes

_WinFuncs_dll = ctypes.CDLL('WinFuncs/WinFuncs.dll')
_WinFuncs_dll.move_cursor_absolute.argtypes = (ctypes.c_short, ctypes.c_short)
_WinFuncs_dll.move_cursor.argtypes = (ctypes.c_short, ctypes.c_short)

def move_cursor(x, y):
    global _WinFuncs_dll
    _WinFuncs_dll.move_cursor(ctypes.c_short(x), ctypes.c_short(y))
    return

def move_cursor_absolute(x, y):
    global _WinFuncs_dll
    _WinFuncs_dll.move_cursor_absolute(ctypes.c_short(x), ctypes.c_short(y))
    return

def mouse_right_up():
    global _WinFuncs_dll
    _WinFuncs_dll.mouse_right_up()
    return

def mouse_right_down():
    global _WinFuncs_dll
    _WinFuncs_dll.mouse_right_down()
    return

def mouse_left_up():
    global _WinFuncs_dll
    _WinFuncs_dll.mouse_left_up()
    return

def mouse_left_down():
    global _WinFuncs_dll
    _WinFuncs_dll.mouse_left_down()
    return