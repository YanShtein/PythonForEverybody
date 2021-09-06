# Exercise 2: Change your socket program so that it counts the number
# of characters it has received and stops displaying any text after it has
# shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count
# of the number of characters at the end of the document.

import socket

webpage = input('Enter website: ')
if len(webpage) < 1:
    webpage = 'http://data.pr4e.org/romeo-full.txt'
try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    domain = webpage.split("/")[2]
    mysock.connect((domain, 80))
    cmd = ('GET ' + webpage + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)
except:
    print('URL is invalid.')
    exit()

data = ''
while True:
    dec = mysock.recv(512)
    if len(dec) < 1:
        break
    data += dec.decode()
mysock.close()

count = 0
for char in data:
    count += 1
    if count < 3000:
        print(char, end='')     # end=" instead of printing every character in new line
print('\nTotal num of characters:', count)
