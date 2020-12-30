#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    mini = 9999999
    prev = arr[0]
    for i,j in enumerate(arr):
        for k,l in enumerate(arr[i+1:]):
            mini = min(mini,abs(j-l),abs(l-j))
        
    return mini
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

