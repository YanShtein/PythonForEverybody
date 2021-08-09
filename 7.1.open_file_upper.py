# Exercise 1: Write a program to read through a file and print the contents
# of the file (line by line) all in upper case.

file = open('mbox-short.txt.txt')
# for each line in file, print in upper case with whitespace removed.
for line in file:
    read = line.upper().strip()
    print(read)
