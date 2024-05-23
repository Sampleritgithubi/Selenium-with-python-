import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()


time.sleep(5)
#We are discuus two commands in browser commands in close() and quit()
#Close()- it will close a specific browser
#Quit()- it will completely close the browser

driver.close()

#driver.quit()
