#Authetication popup/alert- it is used for security purpose for the appln
#we use herokuapp for testing this
#sometimes url and pop will be skipped in that case we need to inject user name and password in url
#syntax for injection
#http://username:password@/test,com
#actual url-http://the-internet.herokuapp.com/basic_auth
#Url with username and pass-  http://admin:admin@the-internet.herokuapp.com/basic_auth
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
#url with username and pass
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")

time.sleep(5)
driver.maximize_window()
driver.quit()