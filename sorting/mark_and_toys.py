#!/bin/python3

import math
import os
import random
import re
import sys

# easy

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    # sort prices from small to large
    sorted_prices = sorted(prices)

    # greedily scan list to get max number of items out of k
    result = 0
    for p in sorted_prices:
        if p <= k:
            result += 1
            k = k - p

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
