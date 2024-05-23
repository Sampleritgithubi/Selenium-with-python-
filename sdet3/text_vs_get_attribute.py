#Text vs Get_Attribute
import time

#Text- 1. text will always return the inner text of the element
#2. Links will have a inner text
#3. We have to use only when we want to capture inner text

#get_Attribute()- 1. Get_Attribute() is a method which will return any value of an attribute of any web element

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")
email=driver.find_element(By.XPATH,"//input[@id='Email']")
email.clear()
email.send_keys("abc@gmail.com")

#Capture text
print("result of text:",email.text)

#capture Get-attribute
print("result of get_attribute",email.get_attribute('value'))
time.sleep(3)

