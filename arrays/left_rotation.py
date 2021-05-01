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

    return a[d:] + a[:d]


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
