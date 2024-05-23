#There many methods to screen shot of web page
#Mostly to check issue where the suite failed
#there are around 5 methods to take screenshot
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os




driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.implicitly_wait(10)
driver.maximize_window()

#Get a screen shot of web page/need to mention a path of project in which user want to save the sceenshot/also name of file
# we also need to import os
#If we dont use path it will be saved in save directory
#--------------------------type-1------------
#driver.save_screenshot(os.getcwd()+"screenshot1.png")

#--------------------------type-2  path of other directory------------
#driver.save_screenshot(os.getcwd()+"path of directory/screenshot1.png")

#----------type-3 (Get screenshot of a file------------------
driver.get_screenshot_as_file(os.getcwd()+"screenshot2.png")

#two more ways of getting screen shot
#4) driver.get_screenshot_as_png  #o/p will be in binary form need to decode the file
#5) driver.get_screenshot_as_base64  #o/p will be in binary form need to decode the file
#above two will be used inforemation is confidencial

