# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 23:22:57 2019

@author: 1
"""


import sys
import requests
import re
from bs4 import BeautifulSoup
import warnings

#warnings.simplefilter("ignore")

url = "http://swallow.5ch.net/livejupiter/subback.html"
#url = "http://example.com/"
#nanJ thread list

html = requests.get(url)
#kore dato mojibake suru
html.encoding = html.apparent_encoding
#moji code wo nantoka sita



#print(type(html.text))


soup = BeautifulSoup(html.text)

name = soup.find_all("a")

for na in name:#この文すごい
    print(na.get_text())

            
            
"""
res = lxml.html.fromstring(html)
res = res.xpath("/html/body/div[2]/small/a[1]")
print(res)



with open("test.txt", 'w', newline='') as f:
    f.write(str(html.text))
"""