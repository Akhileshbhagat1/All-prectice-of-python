import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
PlayFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    PlayFile.write(chunk)
PlayFile.close()