#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    #print(k,sorted(contests))
    ls = []
    contests = sorted(contests)
    luck_bank = 0
    for i in reversed(range(len(contests))):
        
        if(contests[i][1]==0):
            luck_bank+=contests[i][0]
            continue
        
        if(k==0):
            luck_bank-=contests[i][0]
            continue
        else:
            k-=1
            
            luck_bank+=contests[i][0]
            continue
    return (luck_bank)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()

