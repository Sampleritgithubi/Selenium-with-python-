#Mouse action
#Double click
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()

driver.implicitly_wait(10)

#perform right click option on "Register eleemnt"
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick")

#it is inside a frame
driver.switch_to.frame("iframeResult")

#find the element and double click on it
button=driver.find_element(By.XPATH,"//button[@ondblclick='myFunction()']")

#ActionChains operation to perform mouse opeartions
act=ActionChains(driver)

act.double_click(button).perform()

time.sleep(5)
