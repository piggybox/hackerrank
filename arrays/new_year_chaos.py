#!/bin/python3

import math
import os
import random
import re
import sys

# medium

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

# 0, 1, 2, 3, 4
# 2, 1, 5, 3, 4

def minimumBribes(q):
    total_steps = 0
    for i in range(len(q)):
        # bribed too many steps
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        
        # how many bribed in front of q[i]
        # trick here is to limit the range to scan to avoid O(n^2)
        for j in range(max(0, q[i]- 2), i) :
            if q[j] > q[i]:
                total_steps += 1

    print(total_steps)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
