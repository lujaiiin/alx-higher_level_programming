#!/usr/bin/python3
import sys
import random
number = random.randint(-10000, 10000)
last = str(number)
last = last[len(last) - 1]
n = int(last)
if number >= 10000 or number < -10000:
    sys.stderr.write("TypeError\n")
    exit(1)
if number < 0:
    last = '-' + last
    n = n * -1
if n > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif n == 0:
    print(f"Last digit of {number} is {last} and is 0")
elif n <= 5:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
