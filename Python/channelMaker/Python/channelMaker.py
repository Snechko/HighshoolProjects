from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import win32api, win32con
import time
import pyautogui
from pyautogui import *
import keyboard
from pywinauto.application import Application


#PATH VARIABLES
channelPath = "D:\\Desktop\\channelMaker\\Channels\\"
pathToPortableInstaller = "D:\Desktop\channelMaker\Channels\FirefoxPortable85.0.exe"
pathToGeckodriver = "C:\Program Files (x86)\geckodriver.exe"


#INPUT CHANNEL DETAILS
print("Channel name:")
channelName = input()
print("Channel password: ")
channelPass = input()


#PROXY INFO
proxy = "kira.ltespace.com:15554"

firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True

firefox_capabilities['proxy'] = {
    "proxyType": "MANUAL",
    "httpProxy": proxy,
    "ftpProxy": proxy,
    "sslProxy": proxy
}


#FIREFOX PORTABLE INSTALLATION
print("Installing Firefox Portable in the folder " + channelName)
ffp = Application(backend="win32").start(pathToPortableInstaller)
ffp.InstallDialog.NextButton.wait('ready', timeout=60).click_input()
keyboard.write(channelPath  + channelName, delay=0, restore_state_after=True, exact=None)
ffp.InstallDialog.InstallButton.wait('ready', timeout=60).click_input()
ffp.InstallDialog.FinishButton.wait('ready', timeout=60).click_input()


#FIREFOX MANUAL LOGIN
ffp = Application(backend="win32").start(channelPath + channelName + "\\" + "FirefoxPortable.exe")


#FIREFOX PORTABLE RUN THROUGH SELENIUM
print("Launching Firefox...")
options = Options()
options.binary = FirefoxBinary(r'' + channelPath + channelName + '\\App\\Firefox64\\firefox.exe')
options.set_preference("browser.download.folderList",2)
options.add_argument("--start-maximized")
driver = webdriver.Firefox(executable_path=r'' + pathToGeckodriver, options=options, capabilities=firefox_capabilities)
driver.maximize_window()
driver.get("https://youtube.com")
print("Logging in to proxy...")
keyboard.write("ty8m9rvd", delay=0, restore_state_after=True, exact=None)
pyautogui. press("tab")
keyboard.write("oeqh8qsn", delay=0, restore_state_after=True, exact=None)
pyautogui. press("tab")
pyautogui. press("enter")
print("Proxy set-up done")


#ACCOUNT LOGIN
#time.sleep(8)
#def pyClick(x,y):
#    win32api.SetCursorPos((x,y))
#    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
#    time.sleep(0.01)
#    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#pyClick(1860, 100)
#time.sleep(2)

#keyboard.write(channelName + "@gmail.com", delay=0, restore_state_after=True, exact=None)
#pyautogui. press("enter")



#element = WebDriverWait(driver, 10).until(
#        EC.presence_of_element_located((By.ID, "identifierId"))
#    )
#element.send_keys(channelName + "@gmail.com")
#pyautogui. press("enter")

#keyboard.write(channelName + "@gmail.com", delay=0, restore_state_after=True, exact=None)
#driver.get("https://www.google.com/accounts/Login?hl=us&continue=http://www.google.com/")
#element = driver.find_element_by_tag_name("ytd-button-renderer class = 'style-scope ytd-masthead style-suggestive size-small' use-keyboard-focused='' button-renderer='true' is-paper-button-with-icon="" is-paper-button''")
#element.click()
#element = driver.find_element_by_id("identifierId")
#element.send_keys(channelName + "@gmail.com")
#element = driver.find_element_by_id("identifierNext")
#element.click()
#try:
#    element = WebDriverWait(driver, 10).until(
#        EC.presence_of_element_located((By.CLASS_NAME, "style-scope ytd-button-renderer style-suggestive size-small"))
#    )
#    element.click()
#    element = WebDriverWait(driver, 10).until(
#        EC.presence_of_element_located((By.ID, "identifierId"))
#    )
#    element.send_keys(channelName + "@gmail.com")
#    element = WebDriverWait(driver, 10).until(
#        EC.presence_of_element_located((By.ID, "identifierNext"))
#    )
#    element.click()
#except:
#    print("=========Timed out=========")





