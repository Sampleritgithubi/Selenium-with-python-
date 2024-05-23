#Frames/iframes
#frames are nothing but screen splitted in partition in web page # it may many frames in one page or frame inside a frame
#We use switch to frame method here
#switch to deafult to exit from the frame
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

#use switch- driver.switch_to.frame("name of frame")
#find element on the frame and perform the action
#come out of frame- driver.switch_to.default_content()


