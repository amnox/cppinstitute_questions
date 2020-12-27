#!/bin/python3
# Method Used: 
## Create a 2d Matrix
## initialte the first index with 1
## loop through 2D matrix
## ignore empty
## Mark [i+1][j+1] if upper a[i] matches b[j]
## Mark [i+1][j] if a not upper
import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    n, m = len(a), len(b)
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(m+1):
            if not dp[i][j]: continue;
            if j < m and a[i].upper() == b[j]: dp[i+1][j+1] = 1;
            if not a[i].isupper():             dp[i+1][j  ] = 1;
    
    return 'YES' if dp[n][m] else 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()

