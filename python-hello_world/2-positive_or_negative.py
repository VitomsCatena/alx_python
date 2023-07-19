#!/usr/bin/python3
import random

number = random.randint(-10, 10)

signs = {1: "positive", 0: "zero", -1: "negative"}

print("{} is {}".format(number, signs[number >= 0]))


