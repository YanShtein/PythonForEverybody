# Write a function called chop that takes a list and modifies
# it, removing the first and last elements, and returns None.
def chop(lst):               # remove first and last element
    del lst[0]                
    del lst[-1]


# Write a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.
def middle(lst):              # show all elements except first and last. 
    first = lst[1:-1]
    return first


list1 = [10, 20, 30, 40]      # prints None.
a = chop(list1)
print(a)

list2 = [50, 60, 70, 80]      # prints all but the first and last element.
b = middle(list2)
print(b)
