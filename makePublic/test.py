import pyautogui
import time

time.sleep(2)
iml = pyautogui.screenshot(region = (1800, 200, 100 ,880))
iml.save(r"D:\Desktop\makePublic\screen.png")
