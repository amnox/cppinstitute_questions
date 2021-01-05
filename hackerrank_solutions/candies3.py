#!/bin/python3

import math
import os
import random
import re
import sys
# rules for adajacent
## Equal rating can have different candies
## one with less score will have less

# mid cases
## lrger than one smaler than other
def pretty_print(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print( '\n'.join(table))
def candies(n, arr):
    can = [1 for i in range(n)]
    cad = [1 for i in range(n)]
    for i in range(1,n):
        if(arr[i]>arr[i-1]):
            can[i] = can[i-1]+1
    for i in reversed(range(0,n-1)):
        print(i)
        if(arr[i]>arr[i+1]) and (can[i]<=can[i+1]):
            can[i] = can[i+1]+1

    return(sum(can))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
