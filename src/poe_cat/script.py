import pyautogui
import mouse
from .util.windows import *


class Script(object):

    def __init__(self):
        mouse.on_button(self.execute_hold_move, buttons=[mouse.X2], types=[mouse.UP])
        print("[Script]初始化完成")

    def execute_hold_move(self):
        if if_win_active():
            pyautogui.mouseDown(button='left')

    def execute_loop_click_item(self):
        pyautogui.mouseDown(button='left')
