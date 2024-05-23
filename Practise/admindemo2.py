from selenium import webdriver
from selenium.webdriver.common.by import By

#open the chrome browser
driver=webdriver.Chrome()


#open the url
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

driver.implicitly_wait(5)
#find the elements and perform action
driver.find_element(By.NAME, "Email").clear()
driver.find_element(By.NAME, "Email").send_keys("admin@yourstore.com")

driver.find_element(By.NAME, "Password").clear()

driver.find_element(By.NAME, "Password").send_keys("admin")

#click action by using full xpath
driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()


#print the title
print(driver.title)

#comapre the actual and ecpected title

act_title=driver.title
exp_title="Dashboard / nopCommerce administration"

if act_title==exp_title:
    print("Test will pass")
else:
    print("Test failed due to incorrect title")

driver.close()
