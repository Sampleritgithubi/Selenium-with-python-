import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()

driver.get("https://www.google.com/")


driver.maximize_window()

driver.find_element(By.XPATH,"//textarea[@id='APjFqb']").send_keys("selenium")

driver.find_element(By.XPATH,"//textarea[@id='APjFqb']").submit()


#Advanced explicit wait
WebDriverWait(driver,10)
mywait=WebDriverWait(driver,10)
mywait=WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[Exception]



