file_name = input("Enter the file name: ")
# In case the name of the file is invalid exit with a error.
try:
    file_read = open(file_name)
except:
    print('File: "', file_name, '" , cannot be opened.')
    exit()
count = 0
for line in file_read:
    if line.startswith('From:'):            # go over the file, and count each line that starts with the string.
        count = count + 1
print("There were", count, 'subject lines in', file_name)

