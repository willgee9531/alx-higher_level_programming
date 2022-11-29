#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
exe = 0
if number < 0:
    number *= -1
    exe = 1
lastdg = number % 10
if exe == 1:
    number *= -1
    lastdg *= -1
print("Last digit of {:d} is ".format(number), end="")
if lastdg > 5:
    print("{:d} and is greater than 5".format(lastdg))
elif lastdg == 0:
    print("{:d} and is 0".format(lastdg))
else:
    print("{:d} and is less than 6 and not 0".format(lastdg))
