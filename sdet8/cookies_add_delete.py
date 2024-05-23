from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

#Get cookies command
#Capture cookies from browser
cookies=driver.get_cookies()
print("Size of cookies:",len(cookies))

#Check info/details of cookies created by the the browser uing for loop
#using for the loop
#Add the cookies
#using dictionary adding
driver.add_cookie({"name":"mycookies","value":"12345"})
print("Size of cookies:",len(cookies)) #o/p-4
#We need to use get cookies
cookies=driver.get_cookies()
print("size of cookies after adding new one",len(cookies))

#Delete a cookies from the cookies
#specific the name of cookies to be deleted
driver.delete_cookie("mycookie")
#Check no of cookies after deletion
#Again use get cookies to the check fresh update
cookies=driver.get_cookies()
print("Size of cookies after deleting new own:",len(cookies))


#delete the cookies
driver.delete_all_cookies()
cookies=driver.get_cookies()
print("Delete all cookies:",len(cookies)) #all cookies deleted

driver.quit()
