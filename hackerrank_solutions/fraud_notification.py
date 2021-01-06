#!/bin/python3

import math
import os
import random
import re
import sys
import statistics
from bisect import bisect_left, insort_left

def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
 
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
 
 
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

# Complete the activityNotifications function below.
from bisect import bisect_left, insort_left
 
 
def activityNotifications(expenditure, d):
    warnings = 0
     
    running_median = sorted(expenditure[:d])
    for i,ele in enumerate(expenditure):
        if i < d:
            continue
                             
        if d % 2 == 1:
            median = running_median[d//2]
        else:
            median = (running_median[d//2 - 1] + running_median[d//2])/float(2)
             
        if ele >= median*2:
            warnings += 1
             
        # remove previous element
        del running_median[bisect_left(running_median, expenditure[i-d])]
         
        # add new element
        insort_left(running_median, ele)
 
    return warnings

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
