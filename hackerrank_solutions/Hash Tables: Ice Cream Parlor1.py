Function Description

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    cost2 = sorted(cost)
    cutoff = len(cost)-1
    save = (0,0)
    for i,j in enumerate(cost2):
        if(j>=money):
            cutoff = i
    for i in range(0,cutoff+1):
        for j in range(0,cutoff+1):
            if(i==j):
                continue
            if(cost2[i]+cost2[j]==money):
                save = cost2[i],cost2[j]
                break
    
    index1 = cost.index(save[0])
    index2 = cost.index(save[0])+1 if index1==cost.index(save[1]) else cost.index(save[1])
    
    print(min(index1,index2)+1,max(index1,index2)+1)
    return 0
if _name_ == '_main_':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)