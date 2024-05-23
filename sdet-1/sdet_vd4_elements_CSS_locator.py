#Get import files

from selenium import webdriver
from selenium.webdriver.common.by import By


#open chrome
driver=webdriver.Chrome()

driver.get("http://facebook.com/")


driver.maximize_window()
"""
#Tag name is optional but #,., should be there
#type-1 tag and id combo
#Tag and id combo- here tag#id value (input#email)
driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("prashant@gmail.com")

#type-1 tag and class combo
#Tag and class combo- here tag.class value (input#input)
#class value is "inputtext _55r1 _6luy _9npi" there is space in beween values we can ignore value post space
#driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("Ka323437#")

              # or # Tag and id combo
driver.find_element(By.CSS_SELECTOR, "input#pass").send_keys("asv#")
driver.find_element(By.NAME, "login").click()
"""


#3. Tag name and attribute
#syntax- tagname[Attribute=value of attribute] any attribute, tag name is optional, no quotation required
#actual sytax with email example- input[name=email]
driver.find_element(By.CSS_SELECTOR, "input[name=email]").send_keys("ABc")

#4. Tag name,class and attribute- example password
#syntax- tagname.class name[Attribute=value of attribute] any attribute, tag name is optional, no quotation required
#actual sytax with email example- input.inputtext[name=pass]

driver.find_element(By.CSS_SELECTOR, "input.inputtext[name=pass]").send_keys("ABc")


print(driver.title)




