#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    b = list()
    s = sorted(s)
    prev = ''
    for a in s:
        ""
        if(prev==a): continue
        b.append(s.count(a))
        prev = a
    se = set(b)
    if len(se)>1:
        if len(se)>2 : return "NO"
        if(b.count(min(b))==1): return "YES"
        if(b.count(max(b))>1): return "NO"
        #print(b)
        if((max(b)-1)==min(b)):return "YES"
        
        return "NO"
    else:
        return "YES"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

