# This is the first test case
# Open browser chrome
# Importing drivers
# Webdriver is a module which is available in selenium package
from builtins import print
from selenium import webdriver
# import by
from selenium.webdriver.common.by import By

# Open browser chrome by putting path

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


driver.find_element(By.NAME, "username").send_keys("Admin")

driver.find_element(By.NAME, "password").send_keys("admin123")
#find elements on page
#river.find_element_by_name("username").send_keys("Admin")

#driver.find_element_by_name("password").send_keys("admin123")

