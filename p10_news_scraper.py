from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

# get the path of the executable that we will create. we will export the file in the same folder where the executable is
application_path = os.path.dirname(sys.executable)
# datetime will be used to customise the name of the filename
now = datetime.now()
month_day_year = now.strftime("%d-%m-%Y-%H:%M:%S") #string format of the current date and time. Search Python strftime cheatsheet.

website = "https://news.ycombinator.com/news"
path = "/usr/local/bin/chromedriver" # was getting permissions error without this path, it worked with the path

# headless mode
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

# Heading: //div[@class="css-co4v5n"]
containers = driver.find_elements(by="xpath", value='//tr[@class="athing"]')

titles = []
subtitles = []
#links = []

for container in containers:
    title = container.find_element(by="xpath", value='./td/span').text
    subtitle = container.find_element(by="xpath", value='./td/span/a').text
    # link = container.find_element(by="xpath", value='./td/span/a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    # links.append(link)

my_dict = {'Number': titles, 'Headline': subtitles} # 'Link': links
df_headlines = pd.DataFrame(my_dict)

file_name = f'hackernews-headless-date-{month_day_year}.csv'
final_path = os.path.join(application_path, file_name) # join the path of the executable with the name of the file
df_headlines.to_csv(final_path) # customise the name of the file
# pip install pyinstaller
# pyinstaller --onefile p10_news_scraper.py
# SyntaxError: multiple exception types must be parenthesized - Had this bug due to SQLAlchemy. Had to uninstall and reinstall SQLAlchemy. Resolved.

driver.quit()