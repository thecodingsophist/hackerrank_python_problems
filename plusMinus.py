import math
import os
import random
import re
import sys
from decimal import *

# Complete the plusMinus function below.

def decimalCount(decimal, count):
    decimalString = str(decimal)
    decimalCount = 0
    for char in decimalString:
        print("char = ", char)
        if char == '.':
            decimalNum = len(decimalString[decimalCount + 1:])
            break
        decimalCount += 1
    print("decimalNum = ", decimalNum)
    if decimalNum == count:
        print("decimal number equal to count: ", decimal)
        return decimal
    elif decimalNum > count:
        print("decimal number greater than count:", float(decimalString[:decimalCount + 1 + count]))
        return float(decimalString[:decimalCount + 1 + count])
    else:
        while decimalNum != count:
            print("Hello?")
            decimalString += "0"
            print(decimalString)
            decimalNum += 1
        print("decimal number appended with 0's:", float(decimalString))
        return float(decimalString)

def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for num in arr:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zero += 1

    # getcontext().prec = 6
    positive_fraction = Decimal(positive/len(arr))
    negative_fraction = Decimal(negative/len(arr))
    zero_fraction = Decimal(zero/len(arr))

    return print(str(positive_fraction) + "\n" + str(negative_fraction) + "\n" + str(zero_fraction))


if __name__ == '__main__':
    # n = int(input())
    #
    getcontext().prec = 6
    # arr = list(map(int, input().rstrip().split()))
    #
    plusMinus([1,2,3, -1])
    # decimalCount(0.01, 3)
