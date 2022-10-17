import os
from selenium import webdriver

os.environ['PATH'] += r'usr/local/bin/chromedriver' # was getting permissions error without this path, it worked with the path, path where i copied chromedriver to.
driver = webdriver.Chrome()
driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")

driver.implicitly_wait(10) # wait for page to load, we do not want the code to execute before the element is loaded. It does not necessarily wait till the whole duration but waits till it finds the element on the webpage.

my_element = driver.find_element(by="xpath", value="//button[@id='downloadButton']") # find the element
my_element.click()
