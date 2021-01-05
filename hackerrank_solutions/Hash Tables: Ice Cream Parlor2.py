#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    table = {}
    indices = []
    for i in range(1,money):
        table[i] = money-i
    for i in cost:
        if i in table and table[i] == i:
            if(cost.count(i)==1):
                continue
            else:
                indices = [j+1 for j, x in enumerate(cost) if x == i]

                break
        if i in table and table[i] in cost:
            
            indices = [cost.index(i)+1,cost.index(table[i])+1]
            break
    indices = sorted(indices)
    print(indices[0],indices[1])
if __name__ == '__main__':
    t = int(input())
    
    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
