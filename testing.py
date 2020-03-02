#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    points = set()
    special_characters = "!@#$%^&*()-+"

    for char in password:
        if char.isupper():
            points.add("U")
        if char.islower():
            points.add("L")
        if char.isdigit():
            points.add("N")
        if char in special_characters:
            points.add("#")

    print("len points= ", len(points))

    if len(points) == 4 and len(password) < 6:
        return 6 - len(password)
    if len(points) == 4 and len(password) >= 6:
        return 0
    if len(points) < 4 and len(password) < 6:
        if (6 - len(password)) >= (4 - len(points)):
            return (6-len(password))
        if (6 - len(password)) < (4 - len(points)):
            return (4 - len(points))
    if len(points) < 4 and len(password) >= 6:
        return 4 - len(points)


    # for c in points:
    #     print("c", c)
    #     if c in conditionals:
    #         conditionals = conditionals.replace(c, '')
    #         print("conditionals", conditionals)
    #         if len(conditionals) == 0:
    #             break
    # print("points=", points)
    # print("conditionals", conditionals)
    # conditional_points_needed = len(conditionals)
    # return
    # if len(password) < 6:
    #     if 6 - len(password) > conditional_points_needed:
    #         return 6 - len(password)
    #     else:
    #         return 6 - (conditional_points_needed)
    # if len(password) >= 6:
    #     return conditional_points_needed

print(minimumNumber(4, "06HL"))
