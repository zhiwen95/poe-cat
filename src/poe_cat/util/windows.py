
import win32gui

def if_win_active(title='Path of Exile'):
    print(win32gui.GetWindowText(win32gui.GetForegroundWindow()))
    return win32gui.GetWindowText(win32gui.GetForegroundWindow()) == title