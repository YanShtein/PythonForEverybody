# In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
# The program will use urllib to read the HTML from the data files below, 
# extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, 
# follow that link and repeat the process a number of times and report the last name you find.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
cnt = int(input('Enter count: '))
pos = int(input('Enter position: '))
# Set count to -1, to compensate for the first iteration. to fit assignment.
count = -1
while True:
    print('Retrieving: ', url)
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    # Get next URL from tag at user defined pos, update URL value to the next URL.
    # Convert pos to index, by subtracting 1 from user provided pos.
    url = soup('a')[pos-1].get('href')
    count = count + 1
    if count == cnt:
        break
