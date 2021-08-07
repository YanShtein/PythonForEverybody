hrs = float(input("Enter Hours: "))
rph = float(input("Enter Rate: "))

if hrs <= 40:
    print('Pay is:', hrs * rph)
elif hrs > 40:          #if hours entered are over 40
    ohrs = hrs - 40
    orph = ohrs * 1.5 * rph
    pay = (hrs - ohrs) * rph + orph
    print(pay)