score = input("Enter Score: ")

try:
    grade = float(score)
    if 0.9 <= grade <= 1.0:
        print('A')
    elif grade >= 0.8:
        print('B')
    elif grade >= 0.7:
        print('C')
    elif grade >= 0.6:
        print('D')
    elif grade < 0.6:
        print('F')
    else:
        print('bad score')
except:
    print('Error...please enter a number')
    
--------
#Below is the same code with def function added.
--------

score = input("Enter Score: ")


def computegrade(grade):
    try:
        grade = float(score)
        if 1.0 >= grade >= 0.9:
            return "A"
        elif 0.9 > grade >= 0.8:
            return "B"
        elif 0.8 > grade >= 0.7:
            return "C"
        elif 0.7 > grade >= 0.6:
            return "D"
        elif 0.0 < grade < 0.6:
            return "F"
        else:
            return "Bad Score"
    except:
        return 'Error...please enter a number'


print(computegrade(score))

