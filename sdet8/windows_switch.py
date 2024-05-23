#switch the tabs
#switch the windows
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.implicitly_wait(10)
"""
driver.get("https://demo.nopcommerce.com/")
#Switch to new tab
driver.switch_to.new_window('tab')
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
"""


driver.get("https://demo.nopcommerce.com/")
#Switch to windows
driver.switch_to.new_window('window')
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")