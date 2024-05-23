import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#we need to import few more files


driver=webdriver.Chrome()

driver.get("https://www.google.com/")


driver.maximize_window()

driver.find_element(By.XPATH,"//textarea[@id='APjFqb']").send_keys("selenium")

driver.find_element(By.XPATH,"//textarea[@id='APjFqb']").submit()

#Explicit wait basic
WebDriverWait(driver,10)

mywait=WebDriverWait(driver,10)

searchlink=mywait.until(EC.presence_of_element_located(By.XPATH,"//h3[text()='selenium'']"))

time.sleep(5)

