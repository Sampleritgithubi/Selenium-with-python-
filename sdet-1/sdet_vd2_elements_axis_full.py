# Xpath axes (Options)
"""
#Finding elements around the self element
#We can consider any element as self
self
parent
child
ancestor
descendant
following
following sibling
preceding
preceding sibling
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://money.rediff.com/gainers/bse/group")
driver.implicitly_wait(10)
"""
#Self element- Tirupati Tyres
text_msg=driver.find_element(By.XPATH, "//a[normalize-space()='Tirupati Tyres'])/self::a").text
print(text_msg)
"""

"""
#Parent is tr-tag as parent value is 0 value will printed of child
text_msg=driver.find_element(By.XPATH, "//a[normalize-space()='Tirupati Tyres'])/parent::tr").text
print(text_msg)
"""

"""
#child- Ancestor has many childs
#first navigate to ancestor then to child
# We use find_elements as there are many childs
text_msg=driver.find_elements(By.XPATH, "//a[normalize-space()='Tirupati Tyres'])/ancestor::tr/child::tr")
print("text_msg")

"""
