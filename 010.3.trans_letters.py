# Exercise 3: Write a program that reads a file and prints the letters
# in decreasing order of frequency. Your program should convert all the
# input to lower case and only count the letters a-z. Your program should
# not count spaces, digits, punctuation, or anything other than the letters a-z.

import string

x = input('Enter file name: ')
try:
    file = open(x)
except:
    print('Invalid file name.')
    exit()

count = dict()
lst = list()
for line in file:       # lower all letters in line, remove punctuation, digits and whitespaces.
    line = line.lower().translate(line.maketrans('', '', string.punctuation))
    line = line.translate(line.maketrans('', '', string.digits))
    line = line.translate(line.maketrans('', '', string.whitespace))
    for char in line:     # for every character in line, if not exist in dict-> add it, else-> add one to it.
        count[char] = count.get(char, 0) + 1
for key, value in count.items():
    lst.append((key, value))      # add the letter-key and its count-value to a list.
lst = sorted(lst, reverse=False)      # the list will be sorted by key from a-z.
for key, value in lst:
    print(key, value)
