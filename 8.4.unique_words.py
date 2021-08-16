# 8.16 Exercise:
# Download a copy of the file www.py4e.com/code3/romeo.txt.
# Create a list of unique words, which will contain the final result. Write
# a program to open the file romeo.txt and read it line by line. For each
# line, split the line into a list of words using the split function. For
# each word, check to see if the word is already in the list of unique
# words. If the word is not in the list of unique words, add it to the list.
# When the program completes, sort and print the list of unique words
# in alphabetical order.

# romeo.txt :
# But soft what light through yonder window breaks
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief

file = open('romeo.txt')
unique_words = []
for line in file:
    words = line.split()
    for word in words:
        if word in unique_words:
            continue
        unique_words.append(word)
        unique_words.sort()
print(unique_words)
print('finished')
