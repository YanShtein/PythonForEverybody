# Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
# Write a program that reads the words in words.txt and stores them as
# keys in a dictionary. It doesn’t matter what the values are. Then you
# can use the in operator as a fast way to check whether a string is in the
# dictionary.

file = open('words.txt')
counts = dict()
for line in file:
    words = line.split()
    for word in words:
        # set the count of the name for that particular name,
        # get the current count of the name or 0, and add 1 to it.
        counts[word] = counts.get(word, 0) + 1
print(counts.keys())
x = input("Enter a word from file: ")
if x in counts:
    print(True)
else:
    print(False)
