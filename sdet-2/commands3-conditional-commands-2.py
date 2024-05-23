
#now in above object will add click and check is selected or not
# if selected true  / If not false
#this will be explained in next file

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

# we will use nopecommerec demo website
# Register page with male female as option
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")

#is_selected
rd-male=driver.find_element(By.ID,"gender-male")

rd-female=driver.find_element(By.ID,"gender-female")











