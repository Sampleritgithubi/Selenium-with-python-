#findelements()- To find multiple elements
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
"""
#Elements
elements=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
print(len(elements)) #It will return only 1 as we selected one element

#When we use elements we cannot directly use sendkeys
#First we have to extract that element into a variable
#then  indexing that variable
print(elements[0].send_keys("Apple MacBook Pro 13-inch"))

"""

##Condition-2 locator matching with multiple webelement
"""
elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
print(len(elements))
print(elements[0].text)

#if want to print all the names of all the elements
#Using loop statement
for ele in elements:
    print(ele.text)
"""
##Condition3-Element not available nothing will be return - 0 (Zero)
login=driver.find_elements((By.XPATH,"//button[@type='submit']"))
print("elements returned:",len(login))

