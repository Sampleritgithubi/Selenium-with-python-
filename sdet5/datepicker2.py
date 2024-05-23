import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

time.sleep(3)

#select date picker
driver.find_element(By.XPATH,"//input[@id='dob']").click()
time.sleep(3)

#select month from drop down option
datepicker_month=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))

datepicker_month.select_by_visible_text("Dec")

#Select year
datepicker_year=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))

datepicker_year.select_by_visible_text("1995")

#Capture all the date and select the date
alldates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

#for loop to capture all dates
for date in alldates:
    if date.text=="25":
        break
time.sleep(5)
