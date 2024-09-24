# Solve for hacker rank problem "Diagonal Difference"
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    lrSum = 0
    rlSum = 0
    x = len(arr) - 1
    
    for i in range(0, len(arr), 1):
        lrSum += arr[i][i]
        rlSum += arr[i][x]
        x -= 1
    
    if lrSum - rlSum < 0:
        return (lrSum - rlSum) * -1
    else:
        return lrSum - rlSum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
