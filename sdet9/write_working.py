

from selenium import webdriver
from openpyxl import Workbook

# Initialize WebDriver
driver = webdriver.Chrome()

# Open a webpage
driver.get('http://example.com')

# Get some data from the webpage
data_to_write = [
    ["Header 1", "Header 2", "Header 3"],
    ["Data 1", "Data 2", "Data 3"]
]

# Create a new Workbook
workbook = Workbook()

# Create a worksheet
sheet = workbook.active

# Write data to the worksheet
for row in data_to_write:
    sheet.append(row)

# Save the workbook
workbook.save("C:/Users/Admin/Desktop/prashanth/write.xlsx")

# Close the WebDriver
driver.quit()


"""
Type-2
from selenium import webdriver
from openpyxl import Workbook

# Initialize the WebDriver (replace 'chromedriver' with the path to your chromedriver executable)
driver = webdriver.Chrome('chromedriver')

# Open the webpage
driver.get('https://example.com')

# Scraping data from the webpage (Replace these lines with your scraping logic)
data = [
    ["Name", "Age"],
    ["John", "30"],
    ["Alice", "25"],
    ["Bob", "35"]
]

# Create a new Workbook
workbook = Workbook()

# Get the active worksheet
sheet = workbook.active

# Write data to the worksheet
for row in data:
    sheet.append(row)

# Save the workbook
workbook.save("C:/Users/Admin/Desktop/prashanth/write.xlsx")

# Close the WebDriver
driver.quit()

"""