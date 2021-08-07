def computepay(hours, rate):
    if hours > 40:
        ahrs = hours - 40
        arate = ahrs * rate * 1.5
        lpay = (hours - ahrs) * rate + arate
    else:
        lpay = hours * rate
    return lpay


hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))

p = computepay(hours, rate)
print('Pay', p)

