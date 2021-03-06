# Exercise 4: Add code to the above program to figure out who has the
# most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum
# loop (see Chapter 5: Maximum and minimum loops) to find who has
# the most messages and print how many messages the person has.

x = input("Enter a file name: ")
if len(x) < 1:
    x = 'mbox-short.txt'        # for easier access, if pressing Enter, it will default to the file name 'mbox-short.txt'.
try:
    file = open(x)
except:
    print("Enter a valid file name")
    exit()
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
