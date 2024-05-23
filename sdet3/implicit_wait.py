"""
1) Implicit wait
It will be always written below chrome driver opened statement. as it will auto apply to m all statement
It will be killed post clicking the browser by driver.quit()
If element is available within the time limit then it will proceed with the further program execution

advantage
single statement
performance will not be reduced

"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

#implicit wait
driver.implicitly_wait(5)

driver.get("https://www.google.com/")

driver.maximize_window()

driver.find_element(By.XPATH,"//textarea[@id='APjFqb']").send_keys("selenium")

driver.find_element(By.XPATH,"//textarea[@id='APjFqb']").submit()


#//h3[text()="selenium"]

driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()

driver.quit()