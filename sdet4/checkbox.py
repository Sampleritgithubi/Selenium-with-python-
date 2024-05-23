#Check box selection
#Working with checkbox
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(2)

#Select a specific checkbox ex-monday
#Find an element and perform action
#selecting a single checkbox
"""
driver.find_element(By.XPATH,"//input[@id='monday']").click()
"""
driver.maximize_window()
time.sleep(2)

#selecting all check boxes
#Get a common Xpath and select all checkbox
#Every input tag has type=checkbox
#But id is different for all check boxes



#////////Using and operator//////////
#//input[@type='checkbox' and contains[@id='day']]
#using find elements and storing in a variable
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))

"""
#Approach-1
#To select all boxes for loop
for i in range(len(checkboxes)):
    checkboxes[i].click()

#Approach-1
#To select extracting checkbox from checkboxes
for checkbox in checkboxes:
    checkbox.click()
"""
#Selecting check boxes based on user choice
"""
for checkbox in checkboxes:
#using if condition
    weekname=checkbox.get_attribute('id')
    if weekname=='monday' or weekname=='sunday':
        checkbox.click()
"""
#When there are 7 check boxes and user want to select botton two or top two check boxes
#indexing concept will be used here
#formula used-
#(Total no. of elements-2=Starting index)
#7-5=2
"""
for i in range(len(checkboxes)-2,len(checkboxes)):
    checkboxes[i].click()
    """

#selecting first 2 checkboxes (Count from start)
"""
for i in range(len(checkboxes)):
    if i<2:
        checkboxes[i].click()
"""
time.sleep(2)

#Clearing all check box one way is same by select and dis-select statement
"""
driver.find_element(By.XPATH,"//input[@id='monday']").click()
"""

#Clearing all checkboxes at one go
for checkbox in checkboxes:
    checkbox.click()

#Checking if checkbox is already selected then if not slect it
#using for loop and is_selected method
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

driver.quit()
