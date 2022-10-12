from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd

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

my_dict = {'Number': titles, 'Headline': subtitles} # 'Link': links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('hackernews.csv', index=False)

driver.quit()