largest = None			#largest&smallest are outside True-
smallest = None			#-statement to save the input results
while True:
    number = input("Enter a number: ")
    if number == 'done':
        break
    try:
        num = int(number)
    except:
        print('Invalid input')
        continue
    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num

print('Maximum is', largest)
print('Minimum is', smallest)
