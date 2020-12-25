#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    a1 = list(a)
    b1 = list(b)
    b1_len = len(b1)
    switch = []
    if(len(a)<len(b)):
        return "NO"
    j=0
    for i in a1:
        if(j<b1_len):
            if((i==b1[j] or i.capitalize()==b1[j])):
                switch.append(i)
                j = j+1
            else:
                continue
        else:
            if(i.isupper()):
                return "NO"
    #print(switch)
    return "YES" if len(switch)==b1_len else "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()

