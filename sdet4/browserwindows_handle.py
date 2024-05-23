#Browser windows handle is switching b/w different windows on browser
#driver.close()- will close a particular window
#driver.quit()- will close the browser completely
#switch_to.window(WindowID)- window id we get once we open the window
#there is command to get window- current_window.handle (ww will get windowID only for specific window)
#command to get windowId for multiple windows- "window.handles"
import time

#demo-1 (handlewindows)

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()

time.sleep(3)

#store in a variable #get window id
"""
windowid=driver.current_window_handle
print(windowid)
"""
#open one more window
#To open more window click on orange hrm
driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()

#Get window id of both windows
windowIDs=driver.window_handles
#now there are two windows parent and child window #we use indexing to get ids 0,1,2,3
parentwindowid=windowIDs[0]
childwindowid=windowIDs[1]

#print parent child window ids
"""
print(parentwindowid,childwindowid)
"""

# i dont want to print i want to switch b/w parent and child window
#parent to child
driver.switch_to.window(childwindowid)
print(driver.title)

#child to parent window
driver.switch_to.window(parentwindowid)
print(driver.title)