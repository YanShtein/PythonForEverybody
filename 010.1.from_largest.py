# Exercise 1: Revise a previous program as follows: Read and parse the
# “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
# After all the data has been read, print the person with the most commits
# by creating a list of (count, email) tuples from the dictionary. Then
# sort the list in reverse order and print out the person who has the most
# commits.

x = input('Enter file name: ')
try:
    file = open(x)
except:
    print("No such file")
    exit()
count = dict()
for line in file:
    line = line.strip()
    if not line.startswith('From'):
        continue
    words = line.split()
    if len(words) < 3:
        continue
    address = words[1]
    count[address] = count.get(address, 0) + 1
lst = list()
for email, count in count.items():
    lst.append((count, email))
lst = sorted(lst, reverse=True)
for count, email in lst[:1]:
    print(email, count)
