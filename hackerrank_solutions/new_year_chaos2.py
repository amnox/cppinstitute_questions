# https://www.reddit.com/r/learnpython/comments/bsxnqy/why_does_this_answer_succeed_hacker_rank_new_year/
import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.

def minimumBribes(q):
    bribes = 0
    q = [p-1 for p in q]
    for i, p in enumerate(q):
        if p-i > 2:
            print("Too chaotic")
            return
        for j in range(max(p-1,0),i):
            if q[j] > p:
                bribes += 1
    print(bribes)
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
