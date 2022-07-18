import pyautogui
import time

time.sleep(2)
iml = pyautogui.screenshot(region = (100, 100, 100 ,100))
iml.save(r"D:\Desktop\makePublic\screen.png")
