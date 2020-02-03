from bs4 import BeautifulSoup
import requests
import sys

url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
all_movie = soup.find(class_='lister-list').get_text()
title1= all_movie.find(class_='titleColumn').get_text()
print(title1)
# print(tr)
# tr = iter(tr)
# next(tr)
#
# for movie in tr:
#     title = movie.find('td', {'class': 'titleColumn'}).find('a').contents[0]
    # year = movie.find_all('td', {'class': 'titleColumn'}).find('span', {'class': 'secondaryInfo'}).contents[0]
    # rating = movie.find_all('td', {'class': 'ratingColumn imdbRating'}).find('strong').contents[0]
    # row = title + ' - ' + year + ' ' + ' ' + rating

# print(title)