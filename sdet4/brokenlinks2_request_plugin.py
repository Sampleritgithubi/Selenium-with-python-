#handle broken links
#Demo handle broken links
#Website used- http://www.deadlinkcity.com/
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
time.sleep(2)

#Find total no of links
alllinks=driver.find_elements(By.TAG_NAME,'a')
count=0

#Loop statement to check broken links in all links
for link in alllinks:
    url=link.get_attribute('href')
    try:
 # we need hit the request via plugin install om shown below
       res=requests.head(url)
    except:
        None

#verifying
    if res.status_code>=400:
        print(url,"is a broken link")
        count+=1
    else:
        print(url," is a valid link")

print("Total no of broken links:",count) #Total no of broken links

driver.quit()




