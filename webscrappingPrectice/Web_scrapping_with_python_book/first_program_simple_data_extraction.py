# from urllib.request import urlopen
# html = urlopen('http://pythonscraping.com/pages/page1.html')
# print(html.read())

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
bsObj = BeautifulSoup(html.read(), 'lxml')
print(bsObj.h1)
