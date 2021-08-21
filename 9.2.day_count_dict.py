# Exercise 2: Write a program that categorizes each mail message by
# which day of the week the commit was done. To do this look for lines
# that start with “From”, then look for the third word and keep a running
# count of each of the days of the week. At the end of the program print
# out the contents of your dictionary (order does not matter).

file = open('test.txt')
counts = dict()
for line in file:                         # for every line in the file, remove leading and trailing whitespaces
    line = line.strip()
    if not line.startswith('From'):       # if line not starts with From, continue to next iteration-> next line
        continue
    words = line.split()                  # if a line was found, split that line to words
    if len(words) < 3:                    # look for words with length greater than 3
        continue              
    week_day = words[2]                   # search the words in lines for the second position-> the weekday and save them in week_day key.
    counts[week_day] = counts.get(week_day, 0) + 1    # count each day of week, and in case there is None day, add it to dictionary, continue count.
print(counts)
