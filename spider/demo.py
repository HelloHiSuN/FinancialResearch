# coding=utf-8
from urllib import request
from urllib import parse
from bs4 import BeautifulSoup
import ssl
import re

# =================================================================================
# solve the error 'encode_chunked.....'
ssl._create_default_https_context = ssl._create_unverified_context
# =================================================================================

# =================================================================================
# ===urllib test===

# ===get method===
# req = request.Request('http://www.baidu.com')
# resp = request.urlopen(req)
# print(resp.read().decode('utf-8'))

# ===post method===
# req = request.Request('http://www.thsrc.com.tw/tw/TimeTable/SearchResult')
# postData = parse.urlencode([
#     ('StartStationName', '台北站'),
#     ('EndStationName', '台南站'),
#     ('SearchType', 'S'),
#     ('StartStation', '977abb69-413a-4ccf-a109-0272c24fd490'),
#     ('EndStation', '9c5ac6ca-ec89-48f8-aab0-41b738cb1814'),
#     ('DepartueSearchDate', '2018/11/30'),
#     ('DepartueSearchTime', '13:00')
# ])
#
# req.add_header('Origin', 'http://www.thsrc.com.tw')
# req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36')
# resp = request.urlopen(req, data=postData.encode('utf-8'))
# print(resp.read().decode('utf-8'))
# =================================================================================

# =================================================================================
# ===BeautifulSoup test===

# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://exampleScom/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# """
#
# soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())

# print(soup.title.string)
# print(soup.title.get_text())

# print(soup.a)
# print(soup.find(id='link2').string)

# for link in soup.find_all('a'):
#     print(link.string)

# print(soup.find('p', {'class':'story'}).get_text())

# for tag in soup.find_all(re.compile('^b')):
#     print(tag.name)

# for tag in soup.find_all('a', href=re.compile(r'^http://example\.com/')):
#     print(tag.get_text())
# =================================================================================

# =================================================================================
# ===demo===

resp = request.urlopen('https://en.wikipedia.org/wiki/Main_Page').read().decode('utf-8')
soup = BeautifulSoup(resp, 'html.parser')
list_urls = soup.find_all('a', href=re.compile('^/wiki/'))
for url in list_urls:
    print(url.get_text(), '******', url['href'])

# =================================================================================
