# Scraping HTML Data with BeautifulSoup:
# In this assignment you will write a Python program to use urllib to read the HTML from the data files below, 
# and parse the data, extracting numbers and compute the sum of the numbers in the file


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
count = 0
lst = list()
for tag in tags:
    count += 1
    print('TAG:', tag)
    print('URL:', tag.get('comments', None))
    print('Contents:', tag.contents[0])
    lst.append(int(tag.contents[0]))
print('\nCount:', count)
print('Sum:', sum(lst))
