from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

options = Options()
options.binary = FirefoxBinary(r'D:\Desktop\channelMaker\Channels\test\App\Firefox64\firefox.exe')
options.set_preference("browser.download.folderList",2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir","/Data")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/vnd.ms-excel")
driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe', options=options)
driver.get("https://youtube.com")
