# Exercise 1: Write a simple program to simulate the operation of the
# grep command on Unix. Ask the user to enter a regular expression and
# count the number of lines that matched the regular expression:

import re

x = input('Enter file name: ')
file = open(x)
y = input('Enter a word: ')
count = 0
for line in file:
    if re.findall(y, line):
        count += 1
print(x, 'had', count, 'lines that matched', y)
