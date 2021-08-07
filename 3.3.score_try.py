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
