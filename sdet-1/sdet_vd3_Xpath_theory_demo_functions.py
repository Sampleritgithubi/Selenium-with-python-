# complete demo on
# absolute xpath and relative xpath
#funstions or, and, contains() starts_with() and text()

#import all functions

from selenium import webdriver
from selenium.webdriver.common.by import By

#open the browser
driver=webdriver.Chrome()

driver.implicitly_wait(5)
#open the url
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
"""

driver.implicitly_wait(5)
#Absolute and Relative xpath
#For absolute xpath we use copy as full xpath
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.implicitly_wait(5)
#For relative xpath we use copy xpth and verify correctness of xpath with slectorshub plugin
#Attribute should be in single quote ' '
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
driver.implicitly_wait(5)

print(driver.title)

"""

# Xpath functions or options
#there are around 30 to 40 xpath options but only 5 are used widely
# 1. And or OR functions, 2. Contains() functions 3. Starts_with() functions 4.Text()

#1. OR & AND operation use in Xpath

driver.find_element(By.XPATH, "//input[@placeholder='Username' or @name='username']").send_keys("Admin")

#AND opeartor
driver.find_element(By.XPATH, "//input[@placeholder='Password' and @name='Password']").send_keys("admin123")

#click
driver.find_element(By.XPATH, "//button[@type='submit']").click()


# Contains and starts_with() uses
# when we have dynamic elements we need to use this or OR operator
# Example- start and stop button

# //*[constains(@id, 'st')]

# //*[starts_with(@id, 'st')]

# We can also use OR operator

# //*[@id='start' OR @id='stop']

"""
# Text() function
#To find elememt based on text

driver.find_element(By.XPATH, "//a[text()='women']").click()

"""







