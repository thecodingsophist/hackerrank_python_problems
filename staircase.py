import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    if n < 1:
        return
    i = 1
    while i <= n:
        printout = ""
        j = 0
        while j < i:
            printout += "#"
            j += 1
        while (len(printout) < n):
            printout = " " + printout
        print(printout)
        i += 1
    return

if __name__ == '__main__':
    n = int(input())

    staircase(n)
