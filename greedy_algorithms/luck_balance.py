#!/bin/python3

import math
import os
import random
import re
import sys

# easy

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#


def luckBalance(k, contests):
    # sort the luck by order and go from high to low
    # honor constraint: out of important ones, one can lose at most k with largest luck
    max_luck = 0
    imp_count = 0

    sorted_contests = sorted(contests, key=lambda x: -1 * x[0])
    for pair in sorted_contests:
        luck, imp = pair[0], pair[1]
        if imp == 1:
            if imp_count < k:
                imp_count += 1
                max_luck += luck
            else:  # win
                max_luck -= luck
        else:
            max_luck += luck

    return max_luck


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
