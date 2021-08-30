# Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from
# each email address, and print the dictionary.

file = open('test.txt')
count = dict()
for line in file:
    line = line.strip()
    if not line.startswith("From"):
        continue
    words = line.split()
    if len(words) < 3:
        continue
    mail = words[1]
    count[mail] = count.get(mail, 0) + 1
print(count)
