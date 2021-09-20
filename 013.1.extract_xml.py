# Write a Python program which will prompt for a URL, 
# read the XML data from that URL using urllib and then parse 
# and extract the comment counts from the XML data, 
# compute the sum of the numbers in the file.

# Version 1:

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter location: ")
url_read = urllib.request.urlopen(url).read()
content = url_read.decode()
print('Retrieving', url, '\nRetrieved', len(content), 'characters')

data = ET.fromstring(content)
lst = data.findall('comments/comment')
lst_num = list()
for item in lst:
    num = item.find('count').text
    lst_num.append(int(num))
print('Count:', len(lst_num), '\nSum:', sum(lst_num))
--------------------------------------------------------------------------
# Version 2:

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter location: ")
url_read = urllib.request.urlopen(url).read()
content = url_read.decode()
print('Retrieving', url, '\nRetrieved', len(content), 'characters')

data = ET.fromstring(content)
lst = data.findall('.//count')
total = 0
for item in lst:
    count = int(item.text)
    total += count
print(len(lst))
print(total)
