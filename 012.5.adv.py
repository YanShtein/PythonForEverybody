# Exercise 5: (Advanced) Change the socket program so that it only shows
# data after the headers and a blank line have been received. Remember
# that recv receives characters (newlines and all), not lines.

# I used: http://data.pr4e.org/romeo-full.txt
    
import socket

webpage = input('Enter website: ')
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
    decoded = mysock.recv(512)
    if len(decoded) < 1:
        break
    data += decoded.decode()
mysock.close()

pos = data.find('\r\n\r\n')
print(data[pos+2:])    # Plus the two new lines \n\n
