import pandas as pd
import requests
from bs4 import BeautifulSoup
url = requests.get('https://forecast.weather.gov/MapClick.php?CityName=Delhi&state=GA&site=FFC&textField1=33.9136&textField2=-82.6742')


soup = BeautifulSoup(url.text, 'html.parser')
# print(soup.find(class_='forecast-tombstone').get_text())

# print(soup.head)
# print(soup.title)
head_tag = soup.head
# title_tag = head_tag.contents
for child in head_tag.children:
    print(child)























# print(soup.get_text())
# for link in soup.find_all('a'):
#     print(link.get('href'))

# week = soup.find(id='seven-day-forecast-body')

# items = week.find_all(class_='tombstone-container')


# print(items[0].find(class_='period-name').get_text())
# print(items[0].find(class_='short-desc').get_text())
# print(items[0].find(class_='temp-high').get_text())
#
# day = [item.find(class_='period-name').get_text() for item in items]
# descriptions = [item.find(class_='short-desc').get_text() for item in items]
# temperature = [item.find(class_='temp').get_text() for item in items]
# data = list(zip(day, descriptions, temperature))
# for i in data:
#     print(i)
# print(day)
# print(descriptions)
# print(temperature)

# wheather_stuff = pd.DataFrame(
#     {'period': day,
#      'short_decs': descriptions,
#      'temp': temperature}
# )
# print(wheather_stuff)
# wheather_stuff.to_csv('weather.csv')




