#mouse opearations
#right click operation
#we have to right clcik on mouse to perform that particular action
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()

driver.implicitly_wait(10)

#perform right click option on "Register eleemnt"
driver.get("https://www.tutorialspoint.com/about/about_careers.htm")
#to refresh the browser
driver.refresh()
# identifying the source element
source=driver.find_elements(By.XPATH,"//*[text()='Company']")

# action chain object creation
action=ActionChains(driver)
# right click operation and then perform
action.context_click(source).perform()
#to close the browser
driver.close()


#url- for right clcik-  https://swisnl.github.io/jQuery-contextMenu/demo.html
#driver.switch_to.alert.accept() to accept the alert