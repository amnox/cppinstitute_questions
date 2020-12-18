#!/bin/python3

import math
import os
import random
import re
import sys
import statistics
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
def activityNotifications(expenditure, d):
    noti = 0
    n = len(expenditure)-d
    is_even = d%2==0
    d_num = 0
    median = 0
    for a in range(n):
        #sum(expenditure[a:d+a])
        d_num =  expenditure[d+a]
        quickSort(expenditure,a,d+a)
        if(is_even): median = (expenditure[a:d+a][d//2-1]+expenditure[a:d+a][d//2])/2
        else: median = expenditure[a:d+a][d//2]
        if(d_num>=median*2):
            noti=noti+1
        
        #print(expenditure[d+a],median)
    return noti

if __name__ == '__main__':
    fptr = open('input', 'r')
    nd = fptr.read().split()
    
    n = int(nd[0])

    d = int(nd[1])

    expenditure = nd[2:]
    for i in range(0, len(expenditure)):
        expenditure[i] = int(expenditure[i])
    #print(expenditure)
    result = activityNotifications(expenditure, d)

    #fptr.write(str(result) + '\n')
    #print(expenditure)
    fptr.close()

