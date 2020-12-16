#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    l = len(a)
    swaps = 0
    for i in range(l):
        for j in range(l-1):
            if(a[j]>a[j+1]):
                temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp
                swaps = swaps+1
    print("Array is sorted in", swaps,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])
    return swaps
if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

