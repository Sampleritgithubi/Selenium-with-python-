#import files of webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# import By package to find element
#
# Get browser by below code
driver=webdriver.Chrome()

# Get the url og website user wants
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#Find the element

#driver.find_element(By.NAME, "username").send_keys("Admin")
driver.implicitly_wait(5)
driver.find_element(By.NAME, "username").send_keys("Admin")

driver.find_element(By.NAME, "password").send_keys("admin123")





driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()


print(driver.title)
driver.close()


