#Dynamic table
#values inside the box keeps on changing
#orange hrm web site
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)

#find element and input the username and password
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()


#now click on admin
time.sleep(5)
driver.find_element(By.XPATH,"//span[normalize-space()='Admin']").click()
time.sleep(5)

#find total number of rows

