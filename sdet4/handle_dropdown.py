#Drop_down option-
"""
Drop down is a clean method of showing a large lsit of choices since only one choice is displayed initially

"""
import select
import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException


driver=webdriver.Chrome()

driver.get("https://www.opencart.com/index.php?route=account/register")

driver.maximize_window()

time.sleep(15)

"""
#Find the drop down element #dropdown is method which has two many option each option is an element
#storing in variable to use further easily
drpcountry_ele=driver.find_element(By.XPATH,"//select[@id='input-country']")
#select a country
drpcountry=select(drpcountry_ele)
"""

#................OR................
drpcountry=Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))

#select by visible text/options from dropdown
"""
drpcountry.select_by_visible_text("Afghanistan")
drpcountry.select_by_value("10")
drpcountry.select_by_index(17)
"""
#Find total number of drop options available under dropdown section
alloptions=drpcountry.options
print(len(alloptions))

#Print names of all available options
for opt in alloptions:
    print(opt.text)

#select option from drop down without using  built in method/function
for opt in alloptions:


#Using if condition
    if opt.text=="india":
        opt.click()
        break

#Without  using select finding a element and print values of all options
alloptions=driver.find_elements(By.XPATH,'//*[@id="input-country"]/option')
print(len(alloptions))
