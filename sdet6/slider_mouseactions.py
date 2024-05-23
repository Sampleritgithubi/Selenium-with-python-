#mosue actions
#Sliders- seek bar movement similar to e-commerece
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



driver=webdriver.Chrome()
driver.get("https://jqueryui.com/slider/")
driver.implicitly_wait(10)

frame=driver.find_element(By.XPATH,"//*[@id='content']/iframe")
driver.switch_to.frame(frame)


#find location of the slider
slider=driver.find_element(By.XPATH,"//*[@id='slider']/span")

time.sleep(5)

#Now find the location of slider
print("Location before moving.........")
print(slider.location)


#Now move slider postion in x directions
#use ActionChains
act=ActionChains(driver)


act.drag_and_drop_by_offset(slider,70,0).perform()

time.sleep(5)

print("Location after moving...")
print(slider.location)



