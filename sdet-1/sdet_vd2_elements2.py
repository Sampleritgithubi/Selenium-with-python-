# Link text and partia;l link text
# by just knowing the text of value href link before <a>
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")

#Link text and partial link text
#elements how to use
#driver.find_element(By.LINK_TEXT, "Build your own computer").click()

driver.find_element(By.PARTIAL_LINK_TEXT, "Build your own computer").click()
print(driver.title)