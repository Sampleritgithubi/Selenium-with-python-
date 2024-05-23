from selenium import webdriver
from selenium.webdriver.common.by import By

#now open browser

driver=webdriver.Chrome()

#Now open the url
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(5)
#Find element and perform the action
driver.find_element(By.NAME, "username").send_keys("Admin")

driver.find_element(By.NAME, "password").send_keys("admin123")
#click action on login
driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
print(driver.title)
driver.close()

