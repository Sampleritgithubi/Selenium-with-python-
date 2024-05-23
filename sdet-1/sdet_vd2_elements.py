#Find element by id and name
#inspect the element,
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.ID, "small-searchterms").send_keys("HTC One M8 Android L 5.0 Lollipop")

driver.find_element(By.NAME, "q").send_keys("Lenove thinkpad")
driver.close()
