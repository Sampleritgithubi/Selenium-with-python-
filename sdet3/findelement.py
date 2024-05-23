#Find element()- Used to find a single element on web page
#Find elements()- USed to find multiple elements on web page
import time

#1. Condition-1- locator matching with single webelement

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
"""
#Store value in variable or object
# To call when it is needed and to perform action
element=driver.find_element(By.ID,"small-searchterms")
element.send_keys("Apple MacBook Pro 13-inch")
time.sleep(5)
"""

#Condition-2 locator matching with multiple webelement
#Footer links
#//div[@class='footer']//a
"""
element=driver.find_element(By.XPATH,"//div[@class='footer']//a")
element.send_keys("Apple MacBook Pro 13-inch")
print(element.text)  # As it is element it will return only 1st value

"""
#Condition-Element not available then throw Nosuchelementexception
#If i modify submit to subit
login=driver.find_element(By.XPATH,"//button[@type='submit']")
login.click()
time.sleep(5)




