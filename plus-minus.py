# Solve for hacker rank problem 'plus-minus'. Given an array of integers, determine the ratios of positive, negative, and zero integers
# then express as a decimal, formatted to 6 places.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    arrSize = len(arr)
    
    if arrSize == 0:
        return [0,0,0]
    
    posCount = 0
    negCount = 0
    zeroCount = 0
    
    for i in arr:
        if i>0:
            posCount += 1
        elif i==0:
            zeroCount += 1
        elif i<1:
            negCount += 1
    
    return [posCount/arrSize,zeroCount/arrSize,negCount/arrSize]

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    displayList = plusMinus(arr)
    print("{:.6f}".format(displayList[0]))
    print("{:.6f}".format(displayList[2]))
    print("{:.6f}".format(displayList[1]))
