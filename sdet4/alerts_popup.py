#Alerts/ Popup- there are three type of alerts/popup
#There will  be no webelement for alerts
# we need to use "alert" method which is predifined in selenium, as soon as we use alert it will redirect user to opened alert\
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
time.sleep(5)

#1) capture text of the alert window
#2) input value inside the box
#3) ok/cancel the popup
#There will be no web element for popup/alerts---we have to use alert keyword

#we will store it in variable alertwindow
alertwindow=driver.switch_to.alert

print(alertwindow.text)
# we directly send keys
alertwindow.send_keys("Welcome")



#close the pop/alerts
#1) by using ok CTA- "accept"
#alertwindow.accept()  #it click on ok cta- o/p will be printed as welcome

#2)by using cancel cta "dissmis"
alertwindow.dismiss()   #it will click on cancel cta- o/p- Null
time.sleep(3)
