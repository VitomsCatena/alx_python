#!/usr/bin/python3
import random

number = random.randint(-10, 10)

sign = (number > 0) - (number < 0)
signs = {1: "positive", 0: "zero", -1: "negative"}

print("The number is {}".format(signs[sign]))
print(number)

