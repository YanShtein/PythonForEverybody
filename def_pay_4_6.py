x = input("Enter Hours: ")
y = input("Enter Rate: ")


def computepay(hours, rate):
    hours = float(x)
    rate = float(y)

    if hours <= 40:
        return hours * rate
    elif hours > 40:
        over_hours = hours - 40
        over_rate = over_hours * 1.5 * rate
        pay = (hours - over_hours) * rate + over_rate
        return pay


print(computepay(x, y))

