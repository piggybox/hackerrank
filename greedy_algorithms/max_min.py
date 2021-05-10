#!/bin/python3

import math
import os
import random
import re
import sys

# medium 

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


def maxMin(k, arr):
    # sort arr
    sorted_arr = sorted(arr)

    # scan through k-window sequentially
    return min([
        abs(sorted_arr[i + k - 1] - sorted_arr[i])
        for i in range(len(arr) - k + 1)
    ])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
