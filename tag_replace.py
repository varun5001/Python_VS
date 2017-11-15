# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 20:00:17 2017

@author: Varun
"""

from bs4 import BeautifulSoup
import json
soup = BeautifulSoup(open("C:\\cygwin64\\home\\Varun\\test.html"), "html.parser")
print(soup.p.string)
title = soup.h1.string
for tag in soup.find_all('h1'):
    tag.replaceWith('')
with open("output.html", "w") as file:
    file.write(str(soup))
soup_new = BeautifulSoup(open("output.html"), "html.parser")

data = {}
data['title'] = 'title'
data['body'] = str(soup_new)
json_data = json.dumps(data)
print(json_data)
with open("output.json", "w") as file:
    file.write(json_data)
