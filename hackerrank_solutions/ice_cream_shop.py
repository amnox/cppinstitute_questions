#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    hash_table = {}
    for i,j in enumerate(cost):
        if(j in hash_table):
            hash_table[j].append(i+1)
        else:
            hash_table[j] = [i+1]
    for c in cost:
        if((money-c) in hash_table):
            if(c==(money-c)):
                if(len(hash_table[c])>1):
                    print(hash_table[c][0], hash_table[c][1])
                    return
            else:
                print(hash_table[c][0], hash_table[money-c][0])
                return
if __name__ == '__main__':
    t = int(input())
    
    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
