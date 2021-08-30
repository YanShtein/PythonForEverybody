# Exercise 6: Rewrite the program that prompts the user for a list of
# numbers and prints out the maximum and minimum of the numbers at
# the end when the user enters “done”. Write the program to store the
# numbers the user enters in a list and use the max() and min() functions to
# compute the maximum and minimum numbers after the loop completes.

num_list = []
while True:
    number = input("Enter a number: ")
    if number == 'done':
        break
    num_list.append(int(number))
print('Max is:', max(num_list), 'Min is:', min(num_list))
