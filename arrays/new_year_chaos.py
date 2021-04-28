#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    total_steps = 0
    bribe_list = []
    for i in range(len(q)):
        # check if there are bribers after q[i]
        num = len(list(filter(lambda x: x > q[i], bribe_list)))

        if q[i] - (i+1) >= 3:
            print("Too chaotic")
            return
        elif q[i] + num > i :
            bribe_list.append(q[i]) # record briber
            total_steps += q[i] + num - (i + 1)

    print(total_steps)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
