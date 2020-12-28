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
    for i,j in enumerate(arr):
        if (i==n-1):
            break
        if(j<arr[i+1]):
            
            climb = True
            prev = j
            k = i+1
            while(climb):
                if(k==n-1): 
                    break
                if(prev>arr[k]):break
                print(arr[k])
                can[k]+=1
                prev = arr[k]
                k+=1

    if(arr[n-1]>arr[n-2]):
        can[n-1]+=1
    elif((arr[n-2]>arr[n-1]) and (can[n-2]<=can[n-1])):
        can[n-2]+=1

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
