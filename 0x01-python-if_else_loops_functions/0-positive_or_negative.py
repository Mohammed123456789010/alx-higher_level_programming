#!/usr/bin/python3
import random
number = random.randit(-10, 10)
if number > 0:
    print("{:d} is positve".format(number))
elif number < 0:
    print("{:d} is negative".format(number))
else:
    print("{:d} is zero".format(number))
