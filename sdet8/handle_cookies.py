#Handle cookies
"""
Cookies- Whenever user open any website. browser remember the details (Ex-username,pass,eccomerce search
-Cookies have attributes (Name,id) and values and expiry date
-Cookies are dynamic (We cant get same no of cookies)
-Find cookies,delete cookies etc
-Handle coookies

"""
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
for c in cookies:
    #print(c)
#Printing name of a specific cookie and value
    print(c.get('name'))  #Name of the cookies
#PRINTING name and value of the cookies
    print(c.get('name')),":",c.get(('value'))

driver.quit()


