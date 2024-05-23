#We find frames by using find element # inspect #copy as xpath
#Inner frame here there will be frame inside a frame
#parent frame>child frame
#we do not use deafult method to come out of frame
#But in selenium 4.0 option we have an option to come back to parent frame
# application used- https://demo.automationtesting.in/Frames.html
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Frames.html")

#Click the CTA to open frames page
driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

print(driver.title)

#outer frames #store in variable=outerframe #frames does not have name
#We can find frame by Xpath>inspect
outerframe=driver.find_element(By.XPATH,"//*[@id='Multiple']/iframe")
driver.switch_to.frame(outerframe)

#inner frame #store in inner frame #find frame name via xpath as name is not present
innerframe=driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)

time.sleep(5)
#input tesxt in text box in inner frame
driver.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys("welcome")
time.sleep(5)
driver.quit()