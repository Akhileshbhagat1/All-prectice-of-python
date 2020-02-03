from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO

# search = input('Search for :')
# params = {'q': search}
r = requests.get('https://www.bing.com/images/search?q=pizza&FORM=HDRSC2')
# print(r.status_code)

soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
links = soup.findAll('img', {"class": "mimg"})
print(links)
for item in links:
    # print(item.text)
    img_obj = requests.get(item.attrs['href'])
    title = item.attrs["href"].split('/')[-1]
    img = Image.open(BytesIO(img_obj.content))
    # print(img)

    img.save("..\scraped_images" + title, img.formet)
