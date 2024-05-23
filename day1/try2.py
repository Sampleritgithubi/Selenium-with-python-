# This is the first test case
# Open browser chrome
# Importing drivers
# Webdriver is a module which is available in selenium package
from builtins import print

# importing
# from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.common.by import By

# execute test cases on chrome
# from the webdriver module access chrome class
# constructor


driver=webdriver.Chrome()

# driver.get to pass url
#driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") THIS PATH IS NOT NEEDED IN LATEST SELENIUM

driver.implicitly_wait(5)
driver.get("https://www.google.com/")

driver.find_element(By.ID, "APjFqb").send_keys("hello")

driver.find_element(By.NAME, "btnK").click()

driver.find_element(By.CLASS_NAME, "ZxS7Db").click()


