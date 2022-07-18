from pyautogui import *
import keyboard
import time
import random
import win32api, win32con
import pyautogui

#def click(x,y):
#    win32api.SetCursorPos(x,y)
#    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
#    time.sleep(0.01)
#    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while 1:
    if pyautogui.locateOnScreen('editDraft.png', region=(1800, 200, 100, 800), grayscale=True, confidence=0.8) != None:
        print("1")
        time.sleep(1)
    else:
        print("0")
        time.sleep(2)
