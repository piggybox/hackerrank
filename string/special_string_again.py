#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# medium

# Complete the substrCount function below.


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


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
