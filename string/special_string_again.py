#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# medium

# Complete the substrCount function below.

# solution 1: grow from center counting
# O(n^2) complexity
def substrCount(n, s):
    # instead of applying brutual force approach
    # think about the structure of qualified substrings
    # they are symmentric and look like growing from center
    total = 0
    count_sequence = 0 # count the number of consecutive char
    prev = ""

    for i, v in enumerate(s):
        count_sequence += 1
        if i > 0 and prev != v:
            # expand on two sides
            j = 1
            while (i - j >= 0) and (i + j < n) and j <= count_sequence:
                if s[i - j] == prev == s[i + j]:
                    total += 1
                    j += 1
                else:
                    break
            count_sequence = 1

        total += count_sequence # if all equal, basically it's like permutation
        prev = v

    return total

# solution 2: reduce string to char count list
# O(n) complexity
def convert_string(n, s):
    # two pointers approach
    result = []
    prev = s[0]
    count = 1

    for i in range(1, n):
        if s[i] != prev:
            result.append((prev, count))
            prev = s[i]
            count = 1 # reset consecutive count
        else:
            count += 1

    # add the last one
    result.append((prev, count))

    return result

def substrCount(n, s):
    total = 0

    reduced = convert_string(n, s)

    # count substring with same char
    for i in reduced:
        total += i[1] * (i[1] + 1 ) // 2 # permutation

    # count special condition
    for i in range(1, len(reduced) - 1):
        if reduced[i-1][0] == reduced[i+1][0] and reduced[i][1] == 1:
            total += min(reduced[i - 1][1], reduced[i + 1][1])

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
