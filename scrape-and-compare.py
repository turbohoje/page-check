#!/usr/bin/python
import requests
import urllib
import hashlib
import time

#pip install urllib bs4

from bs4 import BeautifulSoup

print "running"

urls = [
"http://www.usajobs.gov/Search/?l=Aurora%2C%20Colorado&k=RN&p=1",
"http://www.usajobs.gov/Search/?l=Aurora%2C%20Colorado&k=RN&p=2"
]

for url in urls:
    print "Fetching " + url
    page = urllib.urlopen(url).read()

    # print hashlib.md5(page).hexdigest()
    print page
    soup = BeautifulSoup(page, "html.parser")
    content = soup.find_all('main').text
    print content
    print hashlib.md5(content).hexdigest()

