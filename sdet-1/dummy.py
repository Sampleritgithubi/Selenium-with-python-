
from selenium import webdriver
from selenium.webdriver.common.by import By

# execute test cases on chrome
# from the webdriver module access chrome class
# constructor
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")



driver.find_element(By.NAME, "username").send_keys("Admin")

driver.find_element(By.NAME, "password").send_keys("admin123")



driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()


print(driver.title)
driver.close()

