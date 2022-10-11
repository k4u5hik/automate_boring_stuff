from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = "https://news.ycombinator.com/news"
path = "/usr/local/bin/chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

# Heading: //div[@class="css-co4v5n"]
containers = driver.find_elements(by="xpath", value='//tr[@class="athing"]')

titles = []
subtitles = []

for container in containers:
    title = container.find_element(by="xpath", value='./td/span').text
    subtitle = container.find_element(by="xpath", value='./td/span/a').text
    titles.append(title)
    subtitles.append(subtitle)

my_dict = {'Number': titles, 'Headline': subtitles}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('hackernews.csv', index=False)

driver.quit()