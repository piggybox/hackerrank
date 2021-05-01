#!/bin/python3

import math
import os
import random
import re
import sys

# medium


# interesting case
# 5 2
# 1 2 1 2 4

# Complete the countTriplets function below.
def countTriplets(arr, r):
    total_count = 0

    # convert array into hash with counts
    hash = {}
    for i in arr:
        hash[i] = hash.get(i, 0) + 1


    # iterate through key to find triplet
    for k in hash:
        # speciaL case on r == 1, permutation of 3 out of n
        if k in hash and r == 1:
            total_count += hash[k] 

        if k * r in hash and k * r * r in hash:
            # add the number of combination to total_count
            total_count += hash[k] * hash[k * r] * hash[k * r * r]

    return total_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
