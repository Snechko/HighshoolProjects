from pyautogui import *
import keyboard
import time
import random
import win32api, win32con
import pyautogui
import sys
from time import sleep



num = 35.2
weight = ""


if keyboard.is_pressed('1'):
    while True:
        num = num + random.uniform(0.1, 2.5)
        weight = str(num)
        print(num)
        for char in weight:
            sleep(0.01)
            sys.stdout.write(char)
            sys.stdout.flush()
        sleep(0.1)
        keyboard.press('enter')
        num = 25.2
        sleep(0.01)
