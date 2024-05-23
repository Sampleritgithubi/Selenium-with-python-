
#we will use rediff web appln for this
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://mypage.rediff.com/login/dologin")

#We will click on login inorder to get the pop
driver.find_element(By.XPATH,"//input[@value='Login']").click()

#Now handle popup.use alert keyword
#we will store alert in variuable alert1

alert1=driver.switch_to.alert

time.sleep(5)

alert1.accept()
driver.quit()