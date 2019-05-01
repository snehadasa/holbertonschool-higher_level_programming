#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def lastDigit(num):
    if num < 0:
        num = -num
    return num % 10

last_Digit = lastDigit(number)
if number < 0:
    last_Digit = -last_Digit
if last_Digit > 5:
    print("Last digit of {} is "
          "{} and is greater than 5".format(number, last_Digit))
elif last_Digit == 0:
    print("Last digit of {} is {} and is 0".format(number, last_Digit))
elif last_Digit < 6:
    print("Last digit of {} is "
          "{} and is less than 6 and not 0".format(number, last_Digit))
