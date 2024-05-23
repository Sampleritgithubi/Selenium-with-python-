#class name and tag name
#it is used to find more than 1 elements
#sometimes there are two many name at that we can use these with indexing
#if we use element instead of elements it will find the first element
#ex- radio button will be to many

from selenium import webdriver
from selenium.webdriver.common.by import By



driver=webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
#to find total number of sliders in the page find common name
slider=driver.find_elements(By.CLASS_NAME, "nivo-imageLink")
print(len(slider))

#tag name to find total number of links (Ex-computer electronics all elements etc)
links=driver.find_element(By.TAG_NAME, "a")
print(len(links))
#o/p total number of links on homepage


