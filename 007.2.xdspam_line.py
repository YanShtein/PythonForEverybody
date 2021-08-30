# Write a program to prompt for a file name, and then read  through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence values from these lines. 
# When you reach the end of the file, print out the average spam confidence.

x = input('Enter file name: ')
file = open(x)
count = 0
total = 0
for line in file:
    word = line.split()         # uses whitespaces to split the words.
    if len(word) != 2:          # if the length of the words in line is not equal to 2, continue to the next iteration, 
        continue                # else go to the next if statement.
    if word[0] != 'X-DSPAM-Confidence:':        # if the first word isnt equal to the string, continue to the next iteration. else, perform next statement.
        continue
    number = float(word[1])         # number equals to the second word, the 0.00000 string. 
    count = count + 1
    total = total + number
average = total/count
print('Average of spam confidence is: ', average)
