import os
from selenium import webdriver

os.environ['PATH'] += os.pathsep + r'usr/local/bin/chromedriver' # was getting permissions error without this path, it worked with the path, path where i copied chromedriver to.
driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.quit()


