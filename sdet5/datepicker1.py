#date picker
#there are 2 types of date formats- 1) standard date 2) Customized date
import time


from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")


#As the date is frame
#Use frame#switch#index as only one frame

driver.switch_to.frame(0)
#xpath- //table[@name='BookTable']/tbody/tr
#//input[@id='datepicker']

#driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("05/30/2024")
time.sleep(3)


#Applying logic
#sending dates/month/year- checking if expected date matches to date or else move to next month until expected and actual date is matched
year="2020"
month="march"
date="30"

#find the date picker element
driver.find_element(By.ID,"datepicker").click()

#capture month and year as it is on top of the dates
#compare actual and expected if does not matches click on next arrow
#if we know start and end point we can use for loop if not we can use
#while loop
#But exit point of while loop needs to be mentioned to exit while loop
while loop:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text


#now compare our expected dates with actual using if conditions

    if mon==month and yr==year:
        break;  #if it match then it will exit the loop or moves to next month

    else:
        # forward arrow to move to future date
      #  driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]").click()

        # backward arrow to move to past date
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]").click()

#Now we need to select the date
#capture all dates from 1 to 31
#using looping

#//div[@id=ui-datepicker-div']//table/tbody/tr/td/a
#------------------Correct one is bel0w---------

#//*[@id="ui-datepicker-div"]/table/tbody/tr/td/a

dates=driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")

for ele in dates:
    if ele.text==date:
        ele.click()
        break

