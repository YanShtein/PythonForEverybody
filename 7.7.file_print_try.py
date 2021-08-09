file_name = input("Enter the file name: ")
# In case the name of the file is invalid exit with a error.
try:
    file_read = open(file_name)
except:
    print('File: "', file_name, '" , cannot be opened.')
    exit()
count = 0
# For every line, if it start with the string count.
for line in file_read:
    if line.startswith('From:'):
        count = count + 1       # count the lines in each iteration with the "string"
print("There were", count, 'subject lines in', file_name)

