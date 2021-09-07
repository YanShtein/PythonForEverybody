# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
# the document from a URL, (2) displaying up to 3000 characters, and
# (3) counting the overall number of characters in the document. Don’t
# worry about the headers for this exercise, simply show the first 3000
# characters of the document contents.

import urllib.request, urllib.error

webpage = input('Enter website: ')
try:
    file = urllib.request.urlopen(webpage)
except:
    print('URL is invalid')
    exit()
count = 0
for line in file:
    words = line.decode()
    for word in words:
        count += 1
        if count < 3000:
            print(word, end='')
print('\n\nOverall number of characters: ', count)
