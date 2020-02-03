import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
import itertools
import re
#
#
# def download(url):
#     print('Downloading :', url)
#     try:
#         html = urllib.request.urlopen(url).read()
#     except (URLError, HTTPError, ContentTooShortError) as e:
#         print('Download Error :', e.reason)
#         html = None
#     return html
# download('http://example.webscraping.com/')


# ###############################################################


def download(url, user_agent='wswp', num_retries=2, charset='utf-8'):
    print('Downloading:', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        resp = urllib.request.urlopen(request)
        cs = resp.headers.get_content_charset()
        if not cs:
            cs = charset
        html = resp.read().decode(cs)
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, num_retries - 1)

    return html


# def crawl_sitemap(url):
#     # download the sitemap file
#     sitemap = download(url)
#     # extract the sitemap links
#     links = re.findall('<loc>(.*?)</loc>', sitemap)
#     # download each link
#     for link in links:
#         html = download(link)
#     return html
#     # scrape html here
#     # ...

# crawl_sitemap('http://example.webscraping.com/sitemap.xml')


# def crawl_site(url):
#     for page in itertools.count(1):
#         pg_url = '{}{}'.format(url, page)
#         html = download(pg_url)
#         if html is None:
#             break
#         # success - can scrape the result
#
#
# crawl_site('http://example.webscraping.com/view/-')


def crawl_site(url, max_errors=5):
    for page in itertools.count(1):
        pg_url = '{}{}'.format(url, page)
        html = download(pg_url)
        num_errors = 1
        if html is None:
            num_errors += 1
            if num_errors == max_errors:
                # max errors reached, exit loop
                break
        else:
            num_errors = 0
            # success - can scrape the result


crawl_site('http://example.webscraping.com/view/-')





