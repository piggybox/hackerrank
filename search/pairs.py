#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


def pairs(k, arr):
    # plan 1:
    # sort array
    # scan array to find diff pairs

    sorted_arr = sorted(arr)
    i, j = 0, 1  # two pointers
    count = 0

    while j < len(arr):
        diff = sorted_arr[j] - sorted_arr[i]

        if diff == k:
            count += 1
            j += 1
        elif diff > k:  # there's no point keep moving j
            i += 1
        elif diff < k:
            j += 1

    return count

    # plan 2:
    # using hash
    # hash = {}
    # for i in arr:
    #     hash[i] = hash.get(i, 0) + 1

    # result = 0
    # for i in hash:
    #     if (i + k) in hash: # avoid double counting
    #         result += 1

    # return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
