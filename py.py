import urllib
import urllib.request
import re

from bs4 import BeautifulSoup

url = 'https://www.mclists.cn/'

webpage = urllib.request.urlopen(url) # 根据超链访问链接的网页

data = webpage.read() # 读取超链网页数据

#print(data)
soup = BeautifulSoup(data, 'html.parser')

strong = soup.find_all('strong')

pattern = re.compile(r'<[^>]+>',re.S)

for s in strong:
    print(s.get_text())

