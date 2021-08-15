# Use a compound logical expression using the or logical operator with a single if statement.

fhand = open('mbox.txt.txt')
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    print('final:', words[2])
