#!/bin/python3

import math
import os
import random
import re
import sys

# easy

# Complete the rotLeft function below.
def rotLeft(a, d):
    # in case d is longer than length of array
    if d > len(a):
        d = d % len(a)

    # shift d times
    for i in range(d):
        temp = a[0]

        # shift to left by 1 position
        for j in range(len(a) - 1):
            a[j] = a[j + 1]

        a[len(a) - 1] = temp

    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
