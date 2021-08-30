# Exercise 2: This program counts the distribution of the hour of the day
# for each of the messages. You can pull the hour from the “From” line
# by finding the time string and then splitting that string into parts using
# the colon character. Once you have accumulated the counts for each
# hour, print out the counts, one per line, sorted by hour.

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
    time = words[5].split(':')
    hour = time[0]
    count[hour] = count.get(hour, 0) + 1
lst = list()
for key, value in count.items():
    lst.append((key, value))
lst = sorted(lst, reverse=False)
for key, value in lst:
    print(key, value)
