"""
Download file
How to automate download file and upload file
It is different for all browser
1. Chrome-just click doenload
2. Edge- just click download
3. Firefox- a pop will open weather user want to open the file or download the file we have to skip that popup via automation

"""
import time

"""Demo-1 (Chrome browser)- 
 We will create a function for browsers and call it based on browser
 """
#imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

# We craete a functions
def chrome_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    return driver
#Open the url
#now call the function
driver=chrome_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/")
driver.maximize_window()

#Find the element on which post clicking user is able to download the file
driver.find_element(By.XPATH,"//a[@href='https://file-examples.com/index.php/sample-documents-download/sample-doc-download/']").click()
#Now reclick on file to be downloaded
time.sleep(5)

driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()
time.sleep(5)


#If user wants to save the file based on user choice
#without changing the default location'
#Copy path of any file "downloads"-downloads- C:\Users\Admin\PycharmProjects\selenium_python\sdet7\downloads
#we need to add few more imports in above imports
#import os
#location=os.getcwd()
#preferences={"download.default_directory":location}
#call chrome option class
ops=webdriver.ChromeOptions()
#add experimental option
#ops=add_experimental.option("prefs",preferences)
#now pass ops in service obj or in chrome
#driver=webdriver.Chrome(options=ops)
#return driver
 

