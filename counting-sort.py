# solve for hacker rank problem "counting sort"
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Create counting array filled with zeroes to increment
    counting_array = []
    for i in range(0, 100, 1):
        counting_array.append(0)
        
    # Now increment them
    for i in range(0, len(arr), 1):
        counting_array[arr[i]] += 1
    
    return counting_array
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
