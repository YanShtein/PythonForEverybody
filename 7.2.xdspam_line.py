# Write a program to prompt for a file name, and then read  through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence values from these lines. 
# When you reach the end of the file, print out the average spam confidence.

file = open('mbox.txt')
# read = file.read()                            Unnesesery, we don't have to read the whole file into memory if we inted to go through it line by line
count = 0
for line in file:                               #changed read directly to file
    line = line.rstrip()
    if 'X-DSPAM-Confidence:' in line:           # changed ...in (read/file) to line because we are only interested in the curent itteration's line
#         continue                              - comented out - The above if-statmen checks wheather the substring we are interested in is in the current line 
#                                               if we continue(to the next line) we skip the work we should do on the target line we just found
    count = count + 1
    print(line, count)
    start_pos = line.find(':')                  # Removed the float() cast because we need the index of ':' as an integer for the next step
    num = line[start_pos+2:]                    # Removed the 5, you ment to go from start_pos+2 to the end of the line the syntacs for this is string[start:[end]]
    extracted = float(num)
print('done, count is: ', count)                # aded the count to the last print statment
# -------------------------------------------- comented this out - *.py files you upload to github shuld be runnable 
fhand = open('mbox.txt')
count = 0
total = 0
for line in fhand:
    words = line.split()
    if len(words) != 2:
        continue
    print('****len words: ', len(words))
    if words[0] != 'X-DSPAM-Confidence:':
        continue
    print('*********dspam: ', words)
#     conf = float(words[1])
#     count = count + 1
#     total = total + conf
# average = total / count
# print('Average spam confidence:', average)
