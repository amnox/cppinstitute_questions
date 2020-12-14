#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    #a = "aaaaaaaaabbb";
    a = sorted(a)
    b = sorted(b)
    delete = 0
    arr_a = sorted(a)
    arr_b = sorted(b)
    for a1 in a:
        if a1 not in arr_b:
            delete = delete+1
            arr_a.remove(a1)
    for b1 in b:
        if b1 not in arr_a:
            delete = delete+1
            arr_b.remove(b1)

    for a1 in arr_a:
        if(arr_a.count(a1)!=arr_b.count(a1)):
            if(arr_a.count(a1)>arr_b.count(a1)):
                print(range(arr_a.count(a1)-arr_b.count(a1)),arr_a.count(a1)-arr_b.count(a1))
                for i in range(arr_a.count(a1)-arr_b.count(a1)):
                    arr_a.remove(a1)
                    delete = delete+1
            else:
                for i in range(arr_b.count(a1)-arr_a.count(a1)):
                    arr_b.remove(a1)
                    delete = delete+1
        
    #print(arr_a,arr_b,delete)
    return delete
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

