#Upload a file
#We will use orange hrm
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
#to identify element
s=driver.find_element(By.XPATH,"//input[@type='file']")
#s = driver.find_element_by_xpath("//input[@type='file']")
#file path specified with send_keys
s.send_keys("C:/Users/Admin/Downloads/SampleJPGImage_50kbmb.jpg")
time.sleep(5)