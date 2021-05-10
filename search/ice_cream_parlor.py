#!/bin/python3

import math
import os
import random
import re
import sys

# medum

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#


def whatFlavors(cost, money):
    # the solution will be unique

    # convert cost into hash to quickly identify tuple in O(n) time
    hash = {}
    for i in cost:
        hash[i] = hash.get(i, 0) + 1

    for k in hash:
        # have to detect duplicate
        if (k == money - k and hash[k] == 2) or (k != money - k and
                                                 (money - k) in hash):
            # found one
            if k < money - k:  # order
                tuple = (k, money - k)
            else:
                tuple = (money - k, k)
            break

    # print(tuple)

    # locate the position of found tuple
    first_flag = False
    result = []
    for i in range(len(cost)):
        if cost[i] == tuple[0] and first_flag == False:
            result.append(str(i + 1))  # 1 based index
            first_flag == True
        elif cost[i] == tuple[1]:
            result.append(str(i + 1))

    print(" ".join(result))


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
