# Exercise 2: Write a program to look for lines of the form:
# New Revision: 39772
# Extract the number from each of the lines using a regular expression
# and the findall() method. Compute the average of the numbers and
# print out the average as an integer.

import re

file = open('mbox.txt')
lst = list()
for line in file:
    x = re.findall('^New Revision: ([0-9]*)', line)
    if len(x) > 0:
        for number in x:
            lst.append(int(number))
average = sum(lst)//len(lst)    # divide by integer division // and round to integer.
print('list: ', lst)
print('sum: ', sum(lst))
print('len: ', len(lst))
print('*** Average is: ', average)
