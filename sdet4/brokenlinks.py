#theory
#There are 3 types of links
"""
1. Internal link- opens in same web page
2. External link- Opens in a new page
3. Broken links- Opens but does not have target page (Sometimes added by developer for future use)

Demo-
every href has a link
Ex- Nopcommerce.com
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")

time.sleep(2)

#Find and click on #href link- #digital downloads
driver.find_element(By.LINK_TEXT,"Digital downloads").click()
print(driver.title)
   #..............Or..................

#driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

#How to find total number links on webpage
#We will store in variable
#all links have anchor tag
links=driver.find_elements(By.TAG_NAME,"a")
print("Total no of links:",len(links))

#-------------or------------
#use of Xpath to find total number of links
links=driver.find_elements(By.XPATH,"//a")
print(len(links))

driver.quit()