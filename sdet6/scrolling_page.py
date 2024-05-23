#Scrolling page
# url- https://www.countries-ofthe-world.com/flags-of-the-world.html
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()

driver.implicitly_wait(10)


driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

"""
#scroll till a certain pixels
driver.execute_script("window.scrollBy(0,3000)","")

#Check how many pixels it moved
value=driver.execute_script("return window.pageYoffset;")
print("number of pixels:",value)
"""

#Sroll till you find the element
flag=driver.find_element(By.XPATH,"//td[normalize-space()='India']")

#now scroll
driver.execute_script("arguments[0].scrollIntoView();",flag)

#Check fixel it moved
value=driver.execute_script("return window.pageYoffset;")
print("number of pixels:",value)


"""
#Scroll tilll the last page

from selenium import webdriver
import time


driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


#Go back to intial page of scroll
time.sleep(5)
driver.execute_script("window.scrollTo(0,-document.body.scrollHeight)")
time.sleep(3)
driver.close()

"""