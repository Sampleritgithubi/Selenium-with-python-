"""
Keybord actions-
to copy and paste a text from box 1 to box2
1. CTRL+A
2. CTRL+C
3. TAB
4. CTRL+V
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()

driver.get("https://text-compare.com/")
driver.implicitly_wait(10)

#capture box 1 and box2
input1=driver.find_element(By.ID,"inputText1")
input2=driver.find_element(By.ID,"inputText2")

#eneter value in box1 (Input1)
input1.send_keys("Welcome to selenium")

#Select the text in input1 box1 and copy that to box1 by switching to input2 box2 by using tab
#use action chains now
act=ActionChains(driver)

#Select text from input box 1
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()

#Copy the text from input box1
act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()

#Move to input box-2 by using tab key
act.send_keys(Keys.TAB)
act.perform()

#Paste the text in input box2
act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()

time.sleep(5)