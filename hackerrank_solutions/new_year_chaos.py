#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.

def minimumBribes(q):
    hops = 0
    for i,n in enumerate(q):
        
        if(i+1<n):
            #print(i+1,n,n-i-1)
            deviation = n-i-1
            if(deviation>=3):
                print("Too chaotic")
                return
            if(deviation==2):
                hops+=2
            else:
                hops+=1
            
    print(hops)
            
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
