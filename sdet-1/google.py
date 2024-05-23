


from selenium import webdriver
from selenium.webdriver.common.by import By

# execute test cases on chrome
# from the webdriver module access chrome class
# constructor


driver=webdriver.Chrome()

driver.implicitly_wait(5)
driver.get("https://www.google.com/")


driver.find_element(By.ID, "APjFqb").send_keys("hello")

driver.find_element(By.NAME, "btnK").click()

driver.find_element(By.CLASS_NAME, "ZxS7Db").click()

##check title through header Google
driver.implicitly_wait(30)

act_title=driver.title
exp_title="Google"

if act_title==exp_title:
    print("Test will pass")
else:
    print("Test failed due to incorrect title")


driver.close()