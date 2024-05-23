#import driver and by package

from selenium import webdriver
from selenium.webdriver.common.by import By

#open the browser
driver=webdriver.Chrome()

#open the url
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

#wait coomand
driver.implicitly_wait(5)

#driver find element
#clear the text from  box before sending values in it
driver.find_element(By.NAME, "Email").clear()
driver.find_element(By.NAME, "Email").send_keys("admin@yourstore.com")

#send password
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")

#logon button
driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()

print(driver.title)

driver.close()
