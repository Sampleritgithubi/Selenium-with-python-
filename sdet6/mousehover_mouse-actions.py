#Mouse actions
#1) Mouse hover
#2)Right click
#3)double clcik
#4)drg and drop
import time

#Demo for mouse hover- placing mouse on an element all the dropdown options will be visible
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/electronics")

#We hover over "computer" element and store it in a variable
com=driver.find_element(By.XPATH,'/html/body/div[6]/div[2]/ul[1]/li[1]/a')
#under drop down select the desktop options
desk=driver.find_element(By.XPATH,"//ul[@class='top-menu notmobile']//a[normalize-space()='Desktops']")

act=ActionChains(driver)

act.move_to_element(com).move_to_element(desk).click().perform()

time.sleep(5)


