#Boostrap dropdown
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

#click on dropdown//ul//li
driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()

#Now check the drop download options and find all drop down options
#customized xpath- //*[@id="select2-billing_country-results"]/li
countrylist=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(countrylist))
time.sleep(5)

#Now using looping statement check for india and select india
for country in countrylist:
    if country.text=="India":
        country.click()
        break  # need to break the

time.sleep(5)
