#!/usr/bin/python3
import random

number = random.randint(-10, 10)

if number > 0:
    sign = "positive"
elif number == 0:
    sign = "zero"
else:
    sign = "negative"

print("{} is {}".format(number, sign))
