#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
absolute_number = abs(number) % 10
if number < 0:
    absolute_number = -absolute_number
    print("Last digit of {} is {} and is ".format(number, absolute_number), end="")
    if absolute_number > 5:
        print("greater than 5")
    elif absolute_number == 0:
        print("0")
    else:
        print("less than 6 and not 0")
