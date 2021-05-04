#!/bin/python3

import math
import os
import random
import re
import sys

# medium


# Complete the countTriplets function below.
def countTriplets(arr, r):
    total_count = 0

    # convert array into hash with counts
    hash = {}
    hash2 = {}  # to record pairs
    for i in range(len(arr) - 1, -1, -1):  # scan in reversed order
        # the order of following operations matters!

        # if arr[i] * r exists in hash2, there must be arr[i]*r*r
        if arr[i] * r in hash2:
            total_count += hash2[arr[i] * r]

        # update pair count
        if arr[i] * r in hash:
            hash2[arr[i]] = hash2.get(arr[i], 0) + hash[arr[i] * r]

        # update count at last to avoid pollution on count with the same pervious number
        hash[arr[i]] = hash.get(arr[i], 0) + 1

        # print(arr[i], hash, hash2)

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
