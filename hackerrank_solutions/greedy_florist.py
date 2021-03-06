#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    p = [0]*k
    price = 0
    #print(c)
    c = sorted(c)
    for i in reversed(range(len(c))):
        index = p.index(min(p))
        price += (p[index]+1)*c[i]
        p[index] +=1
    return(price)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()

