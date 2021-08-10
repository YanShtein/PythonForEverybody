x = input('Enter file name: ')
if x == 'na na booboo':
    print('NA NA BOO BOO TO YOU - You have been punkd!')
    exit()
try:
    file = open(x)
except:
    print('Error, no such file')
    exit()
count = 0
total = 0
for line in file:
    word = line.split()
    if len(word) != 2:
        continue
    if word[0] != 'X-DSPAM-Confidence:':
        continue
    number = float(word[1])
    count = count + 1
    total = total + number
average = total/count
print('Average of spam confidence is: ', average)
