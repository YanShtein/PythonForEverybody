# Exercise 4: Add code to the above program to figure out who has the
# most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum
# loop (see Chapter 5: Maximum and minimum loops) to find who has
# the most messages and print how many messages the person has.

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
big_word = None
big_count = None
for mail, count in count.items():
    if big_count is None or count > big_count:
        big_count = count
        big_word = mail
print(big_word, big_count)
