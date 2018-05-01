# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 17:26:12 2018

@author: araveret
"""

import requests
url = r'https://www.realclearpolitics.com/epolls/latest_polls/'
r = requests.get(url)

# convert HTML into a structured Soup object
from bs4 import BeautifulSoup
b = BeautifulSoup(r.text)

b.find_all('td', attrs={'class':'date'})[0].text
