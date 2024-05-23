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


driver=webdriver.Chrome("C:/Users/Adop/Selenium_Python/drivers/chromedriver-win64/chromedriver-win64/chromedriver.exe")

#open url
# driver.get to pass url
#driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") THIS PATH IS NOT NEEDED IN LATEST SELENIUM

driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com")

driver.find_element(By.NAME, "username").send_keys("Admin")

driver.find_element(By.NAME, "password").send_keys("admin123")

driver.find_element(By.XPATH("//button[normalize-space()='Login']"))

#driver.find_element(By.CLASS_NAME,
# "oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()