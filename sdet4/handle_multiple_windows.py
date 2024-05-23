#When number of windows are more
#then we can use loop statement
import time

#demo-1 (handlewindows)

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()

time.sleep(3)
#open one more window
#To open more window click on orange hrm
driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()

#Get window id of both windows
windowIDs=driver.window_handles

#Use of looping approach when number of windows are more ex-10
for winid in windowIDs:
    driver.switch_to.window(winid)
    print(driver.title) # get title of the window

#close a specific browser window based on users choice
#same looping method we will use
# we have the mention the title of page
for winid in windowIDs:
    driver.switch_to.window(winid)
#we have to mention the "title" of the window #we can find it via inspect
    if driver.title=="OrangeHRM":
        driver.close()