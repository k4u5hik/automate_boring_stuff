from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = "https://www.thesun.co.uk/sport/football/"
path = "/usr/local/bin/chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

# Heading: //div[@class="css-co4v5n"]
containers = driver.find_elements(by="xpath", value='//div[@class="css-co4v5n"]')

titles = []
subtitles = []

for container in containers:
    title = container.find_element(by="xpath", value='./h3').text
    subtitle = container.find_element(by="xpath", value='./section/h2/span').text
    titles.append(title)
    subtitles.append(subtitle)

my_dict = {'titles': titles, 'subtitles': subtitles}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headlines.csv', index=False)

driver.quit()