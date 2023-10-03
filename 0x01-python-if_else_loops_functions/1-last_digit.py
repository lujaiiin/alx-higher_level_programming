#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
#last = str(number)
#last = last[len(last) - 1]
#n = int(last)
#n = number % 10
if number < 10:
    n = number % -10
else:
    n = number % 10
#  last = '-' + last
 #   n = n * -1//
if n > 5:
    print(f"Last digit of {number} is {n} and is greater than 5")
elif n == 0:
    print(f"Last digit of {number} is {n} and is 0")
elif n <= 5:
    print(f"Last digit of {number} is {n} and is less than 6 and not 0")
