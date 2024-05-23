#Headless testing- testing will be done in backend nothing will be visible
#TEsting case execution will be background
from selenium import webdriver


#Creating a function
def headless_chrome():
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.headless = True
    driver=webdriver.Chrome()
    return driver
#Call the driver function
driver=headless_chrome()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
print(driver.title)
print(driver.current_url)
driver.close()
