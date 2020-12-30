#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference1(arr):
    mini = 9999999
    prev = arr[0]
    for i,j in enumerate(arr):
        for k,l in enumerate(arr[i+1:]):
            mini = min(mini,abs(j-l),abs(l-j))
        
    return mini


def minimumAbsoluteDifference(arr): 
    n = len(arr)
    # Sort array in non-decreasing order 
    arr = sorted(arr) 
  
    # Initialize difference as infinite 
    diff = 10**20
  
    # Find the min diff by comparing adjacent 
    # pairs in sorted array 
    for i in range(n-1): 
        if arr[i+1] - arr[i] < diff: 
            diff = arr[i+1] - arr[i] 
  
    # Return min diff 
    return diff 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
