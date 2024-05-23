#Opening of tab and windows
#Opening of tabs link in new window
#by using keyboard keys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
#manual approach to open window in same tab
#driver.find_element(By.XPATH,"//a[@class='ico-register']").click()


#Opening the link in new tab
#store that in a variable

reglink=Keys.CONTROL+Keys.RETURN
driver.find_element(By.XPATH,"//a[@class='ico-register']").send_keys(reglink)

time.sleep(3)




