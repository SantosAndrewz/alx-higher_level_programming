#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    ld = number % 10
else:
    ld = (((number * -1) % 10) * -1)
msg = "Last digit of {} is {} and is ".format(number, ld)

if ld > 5:
    print(msg + "greater than 5")
elif ld == 0:
    print(msg + "0")
else:
    print(msg + "less than 6 and not 0")
