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
    print(arr)
    can = [[1 for i in range(n)] for j in range(n)]
    min_score = min(arr)
    max_score = max(arr)
    #can[0][0] = 1
    for i in range(n):
        for j in range(n):
            ""
            if(j==0):
                ""
                if(arr[j]>arr[j+1]):
                    can[i][j]+=1
                if((arr[j]==arr[j+1]) and (can[i][j]>=2)):
                    can[i][j]-=1
                continue
            if(j==n-1):
                ""
                if(arr[j]>arr[j-1]):
                    can[i][j]+=1
                if((arr[j]==arr[j-1]) and (can[i][j]>=2)):
                    can[i][j]-=1
                continue
            else:
                if(arr[j]>arr[j-1] and arr[j]>arr[j+1]):
                    can[i][j]+=1
                    continue
                if(arr[j]>arr[j-1] and arr[j]<arr[j+1]):
                    if(can[i][j+1]==can[i][j]):
                        can[i][j+1]+=2
                        can[i][j]+=1
                    elif(can[i][j+1]<can[i][j]):
                        can[i][j+1]= can[i][j]
                    continue
                if(arr[j]<arr[j-1] and arr[j]>=arr[j+1]):
                    if(can[i][j+1]==can[i][j]):
                        can[i][j]+=1
                    continue
    pretty_print(can)           
    return sum(can[n-1])        
    
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
