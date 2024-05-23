# Conditional commands
#Used for check box or radio button
#is_displayed()-  o/p- it will give false if disabled
#is_enabled()-  o/p- it will give True if enabled
#is_selected()- Check checkbox/radio button is selected or not (selected-True / Not selected-False)

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

# we will use no ecommerec website
driver.get("https://demo.nopcommerce.com/")

#Search box
searchbox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']").click()

# use print #is displayed
print(searchbox.is_displayed())  #o/p- true as it is displayed


# use print #is enabled
print(searchbox.is_enabled())  #o/p- true as it is enabled


#now in above object will add click and check is selected or not
# if selected true  / If not false
#this will be explained in next file




