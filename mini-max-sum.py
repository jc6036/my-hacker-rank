# Solve for HackerRank problem "Mini-Max Solve"
# In: array of 5 integers
# Out: the smallest sum of 4 possible, and largest sum of 4 possible

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    
    low = arr[0]+arr[1]+arr[2]+arr[3]
    high = arr[1]+arr[2]+arr[3]+arr[4]
    
    print("{} {}".format(low, high))
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
