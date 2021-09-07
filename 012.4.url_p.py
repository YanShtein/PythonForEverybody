# Exercise 4: Change the urllinks.py program to extract and count paragraph (p) tags from the retrieved HTML document and display the
# count of the paragraphs as the output of your program. Do not display
# the paragraph text, only count them. Test your program on several
# small web pages as well as some larger web pages.


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

webpage = input('Enter webpage: ')
html = urllib.request.urlopen(webpage).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('p')
count = 0
for tag in tags:
    count += 1
print('Number of paragraphs: ', count)
