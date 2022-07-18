from pyautogui import *
import keyboard
import time
import random
import win32api, win32con
import pyautogui

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while True:
    if keyboard.is_pressed("1"):
        click(1442, 919)
        print("Next")
        time.sleep(0.1)
    if keyboard.is_pressed("2"):
       click(565, 691)
       print("Bullet1")
       time.sleep(0.1)
    if keyboard.is_pressed("1"):
        click(1442, 919)
        print("Next")
        time.sleep(0.1)
    if keyboard.is_pressed("1"):
        click(1442, 919)
        print("Next")
        time.sleep(0.1)
    if keyboard.is_pressed("2"):
        click(565, 691)
        print("Bullet2")
        time.sleep(0.1)
    if keyboard.is_pressed("1"):
        click(1442, 919)
        print("Next")
        time.sleep(0.1)
    if keyboard.is_pressed("3"):
        click(1189, 802)
        print("Close")
        time.sleep(0.1)
#    time.sleep(0.5)
