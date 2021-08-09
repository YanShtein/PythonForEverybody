file = open('mbox-short.txt.txt')
# for each line in file, print in upper case with whitespace removed.
for line in file:
    read = line.upper().strip()
    print(read)
