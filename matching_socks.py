#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    sorted = {}
    for n in ar:
        if n in sorted:
            sorted[n] += 1
        else:
            sorted[n] = 1

    print(sorted)

    count = 0
    for key in sorted:
        if sorted[key]%2 == 0:
            count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
