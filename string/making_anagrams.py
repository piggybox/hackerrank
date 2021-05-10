#!/bin/python3

import math
import os
import random
import re
import sys

# easy

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    # 1. sort two strings
    sorted_a = sorted(a)
    sorted_b = sorted(b)

    # 2. compare sorted strings from start with two pointers to find out difference
    i, j = 0, 0
    difference = 0

    while i < len(a) and j < len(b):
        if sorted_a[i] == sorted_b[j]:
            # test next positions
            i += 1
            j += 1
        elif sorted_a[i] < sorted_b[j]:
            difference += 1
            i += 1
        else:
            difference += 1
            j += 1

    # add what's left in i or j
    if i < len(a):
        difference += len(a) - i
    else:
        difference += len(b) - j

    return difference


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
