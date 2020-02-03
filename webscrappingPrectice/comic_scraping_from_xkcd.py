import requests, os
from bs4 import BeautifulSoup

url = 'http://xkcd.com'
os.makedirs('xkcd_data', exist_ok=True)
count = 0
while not url.endswith('#'):
    count += 1
    print('downloading page %s....' % url, count)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('could not find comic images.')
    else:
        comicUrl = comicElem[0].get('src').strip("http://")
        comicUrl = "http://" + comicUrl
        if 'xkcd' not in comicUrl:
            comicUrl = comicUrl[:7]+'xkcd.com/' + comicUrl[7:]
        print('Downloading images %s...' % comicUrl)
        res1 = requests.get(comicUrl)
        res1.raise_for_status()
        imageFile = open(os.path.join('xkcd_data', os.path.basename(comicUrl)), 'wb')
        for chunk in res1.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')
        print("Done")






