# Exercise 5: This program records the domain name (instead of the
# address) where the message was sent from instead of who the mail came
# from (i.e., the whole email address). At the end of the program, print
# out the contents of your dictionary.

# In this exercise we will need to use "From" full lines, such as: 'From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008'
# and not these: 'From: zqian@umich.edu'

# Following the output example from the exercise: 
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

x = input('Enter a file: ')
try:
    file = open(x)
except:
    print("Please enter a valid file name.")
    exit()
count = dict()
for line in file:
    line = line.strip()
    if not line.startswith("From"):
        continue
    words = line.split()
    if len(words) < 3:      # using only these lines: 'From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008' for the exercise.
        continue
    word = words[1].split('@')
    domain = word[1]
    count[domain] = count.get(domain, 0) + 1
print(count)
