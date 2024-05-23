import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://snapdeal.com/")

driver.get("https://www.amazon.com/")

#There 3 things
"""
1. back()
2. forward()
3.refresh()
"""
driver.back()

driver.forward()


driver.refresh()

time.sleep(5)

driver.quit()