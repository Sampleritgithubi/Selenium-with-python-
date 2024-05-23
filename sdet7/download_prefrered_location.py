from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()

prefs = {"download.default_directory" : "C:\YourDirectory\Folder"}

options.add_experimental_option("prefs", prefs)


class ChromeDriverManager:
    pass


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


#Need to study more
