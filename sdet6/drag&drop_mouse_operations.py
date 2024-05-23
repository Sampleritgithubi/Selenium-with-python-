#Mouse actions
#Drag and Drop operations
#example of a capital dropping to country

import time





from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
drag = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[starts-with(@id, 'box') and text()='Rome']")))
drop = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[starts-with(@id, 'box') and text()='South Korea']")))
ActionChains(driver).drag_and_drop(drag, drop).perform()
time.sleep(5)