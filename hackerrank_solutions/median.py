#!/bin/python3

import math
import os
import random
import re
import sys
import statistics

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    noti = 0
    for a in range(len(expenditure)-d):
        #sum(expenditure[a:d+a])
        if(2*statistics.median(expenditure[a:d+a])<=expenditure[d+a]): noti=noti+1
    #print(noti)
    return noti

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()

