#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number == str(number):
    print("TypeError")
last = str(number)
last = last[len(last) - 1]
n = int(last)
if number < 0:
    last = '-' + last
    n = n * -1
if n > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif n == 0:
    print(f"Last digit of {number} is {last} and is 0")
elif n <= 5:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
